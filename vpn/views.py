from urllib.parse import urlparse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from vpn.forms import SiteCreateForm

from vpn.models import Site


class SiteListView(LoginRequiredMixin, ListView):
    model = Site
    template_name = "vpn/site_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@login_required
def site_create_view(request):
    if request.method == "GET":
        form = SiteCreateForm()
        return render(request, "vpn/site_create.html", context={"form": form})
    elif request.method == "POST":
        form = SiteCreateForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            _, domain, endpoint, *_ = urlparse(url)
            site = Site(domain=domain, endpoint=endpoint, user=request.user)
            site.save()
            return redirect("vpn:site_list")
        return render(request, "vpn/site_create.html", {"form": form})
