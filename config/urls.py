from django.contrib import admin
from django.urls import include, path

from user.views import LogoutConfirmation, UserRegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls", namespace="user")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", UserRegisterView.as_view(), name="register"),
    path(
        "accounts/confirm-logout/", LogoutConfirmation.as_view(), name="confirm_logout"
    ),
    path("", include("vpn.urls", namespace="vpn")),
]
