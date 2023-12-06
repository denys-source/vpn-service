from django.urls import path

from user.views import LogoutConfirmation, UserDetailView, UserUpdateView


urlpatterns = [
    path("profile/", UserDetailView.as_view(), name="profile"),
    path("profile/update/", UserUpdateView.as_view(), name="update_profile"),
    path(
        "confirm-logout/", LogoutConfirmation.as_view(), name="confirm_logout"
    ),
]

app_name = "user"
