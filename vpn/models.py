from urllib.parse import urljoin

from django.conf import settings
from django.db import models


class Site(models.Model):
    domain = models.CharField(max_length=63)
    endpoint = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="sites",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"http://{urljoin(self.domain, self.endpoint)}"
