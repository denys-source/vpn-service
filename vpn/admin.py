from django.contrib import admin

from vpn.models import Site, Statistics


admin.site.register(Site)
admin.site.register(Statistics)
