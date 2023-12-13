from urllib.parse import urljoin

from django.conf import settings
from django.db import models


class Statistics(models.Model):
    domain = models.CharField(max_length=63)
    page_clicks = models.PositiveIntegerField(default=0)
    data_received = models.FloatField(default=0)
    data_sent = models.FloatField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="statistics",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ("domain", "user")
        ordering = ("-page_clicks",)
        verbose_name_plural = "statistics"

    def __str__(self) -> str:
        return f"Statistics for {self.domain}"


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
        return urljoin(f"http://{self.domain}", self.endpoint)
