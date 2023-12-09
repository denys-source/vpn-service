from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from django.http.request import HttpRequest
from django.urls import reverse
from requests import Response

from vpn.models import Statistics


class LinkUpdater:
    def __init__(
        self, soup: BeautifulSoup, domain: str, endpoint: str
    ) -> None:
        self._soup = soup
        self._domain = domain
        self._endpoint = endpoint
        self._base_url = urljoin(f"http://{domain}/", endpoint)

    def _is_absolute(self, url: str) -> bool:
        return bool(urlparse(url).netloc)

    def _update_href_links(self) -> None:
        for element in self._soup.find_all(href=True):
            url = element["href"]
            if element.name != "link":
                if self._is_absolute(url):
                    _, link_domain, link_endpoint, *_ = urlparse(url)
                    if link_domain == self._domain:
                        element["href"] = reverse(
                            "vpn:proxy",
                            kwargs={
                                "domain": self._domain,
                                "endpoint": link_endpoint,
                            },
                        )
                else:
                    element["href"] = reverse(
                        "vpn:proxy",
                        kwargs={
                            "domain": self._domain,
                            "endpoint": urljoin(self._endpoint, url),
                        },
                    )
            elif not self._is_absolute(url):
                element["href"] = urljoin(self._base_url, url)

    def _update_link_attribute(self, attr_name: str) -> None:
        for element in self._soup.find_all(attrs={attr_name: True}):
            url = element[attr_name]
            if not self._is_absolute(url):
                element[attr_name] = urljoin(self._base_url, url)

    def _update_src_links(self) -> None:
        self._update_link_attribute("src")

    def _update_action_links(self) -> None:
        self._update_link_attribute("action")

    def update_links(self) -> BeautifulSoup:
        self._update_href_links()
        self._update_src_links()
        self._update_action_links()
        return self._soup


def update_statistics(
    request: HttpRequest, response: Response, domain: str
) -> None:
    statistics, _ = Statistics.objects.get_or_create(
        domain=domain, user=request.user
    )

    data_sent = len(response.request.body or "")
    data_received = len(response.content)
    statistics.page_clicks += 1
    statistics.data_sent += data_sent
    statistics.data_received += data_received
    statistics.save()
