from django.urls import path, register_converter

from vpn.converters import SlashStrip
from vpn.views import SiteListView, site_create_view, proxy_view


register_converter(SlashStrip, "slashstrip")

urlpatterns = [
    path("sites/", SiteListView.as_view(), name="site_list"),
    path("sites/create/", site_create_view, name="site_create"),
    path("<str:domain>/<slashstrip:endpoint>", proxy_view, name="proxy"),
]

app_name = "vpn"
