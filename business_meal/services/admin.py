from django.contrib import admin
from django.contrib.sites.models import Site
from unfold.admin import ModelAdmin, StackedInline

admin.site.unregister(Site)
# admin.site.unregister(Country)
# admin.site.unregister(Region)
# admin.site.unregister(City)
# admin.site.unregister(SubRegion)
# admin.site.unregister(Payment)
