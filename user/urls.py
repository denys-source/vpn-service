from django.urls import path

from user.views import (
    UserDetailView,
    UserUpdateView,
)


urlpatterns = [
    path("profile/", UserDetailView.as_view(), name="profile"),
    path("profile/update/", UserUpdateView.as_view(), name="update_profile"),
]

app_name = "user"
