from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls", namespace="user")),
    path("accounts/", include("django.contrib.auth.urls")),
]
