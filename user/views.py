from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, UpdateView


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ["first_name", "last_name", "email"]
    template_name = "user/update_profile.html"
    success_url = reverse_lazy("user:profile")

    def get_object(self, queryset=None):
        return self.request.user


class LogoutConfirmation(TemplateView):
    template_name = "registration/logout_confirmation.html"
