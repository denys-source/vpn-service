from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView
from requests.exceptions import RequestException

from vpn.forms import SiteCreateForm
from vpn.models import Site
from vpn.utils import LinkUpdater


class SiteListView(LoginRequiredMixin, ListView):
    model = Site
    template_name = "vpn/site_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@login_required
def site_create_view(request: HttpRequest):
    if request.method == "GET":
        form = SiteCreateForm()
        return render(request, "vpn/site_create.html", context={"form": form})
    elif request.method == "POST":
        form = SiteCreateForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            _, domain, endpoint, *_ = urlparse(url)
            site = Site(
                domain=domain, endpoint=endpoint, user=request.user
            )
            site.save()
            return redirect("vpn:site_list")
        return render(request, "vpn/site_create.html", {"form": form})


@login_required
def proxy_view(request: HttpRequest, domain: str, endpoint: str):
    url = f"{urljoin(f"http://{domain}/", endpoint)}"
    try:
        resp = requests.get(url)
    except RequestException:
        return HttpResponseBadRequest() 
    raw_soup = BeautifulSoup(resp.content, "html.parser")
    updater = LinkUpdater(soup=raw_soup, domain=domain, endpoint=endpoint)
    soup = updater.update_links()
    return HttpResponse(str(soup))
