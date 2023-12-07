from django.urls import path

from vpn.views import site_create_view, SiteListView


urlpatterns = [
    path("sites/", SiteListView.as_view(), name="site_list"),
    path("sites/create/", site_create_view, name="site_create"),
]

app_name = "vpn"
