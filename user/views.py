from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    TemplateView,
    UpdateView,
)

from user.forms import RegisterForm


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "user/profile_detail.html"

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ["first_name", "last_name", "email"]
    template_name = "user/update_profile.html"
    success_url = reverse_lazy("user:profile")

    def get_object(self, queryset=None):
        return self.request.user


class LogoutConfirmation(LoginRequiredMixin, TemplateView):
    template_name = "registration/logout_confirmation.html"


class UserRegisterView(CreateView):
    model = get_user_model()
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
