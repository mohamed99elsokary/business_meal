from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin

from ..addonsapp.admin import FilterForUserAdmin
from . import models


@admin.register(models.OpenBuffetPackage)
class OpenBuffetPackage(FilterForUserAdmin, ModelAdmin, TranslationAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == "restaurant":
            kwargs["queryset"] = models.Restaurant.objects.filter(
                admin=request.user, is_open_buffet=True
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ("name", "restaurant")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(restaurant__admin=request.user)


@admin.register(models.OpenBuffetPackageOptions)
class OpenBuffetPackageOptionsAdmin(FilterForUserAdmin, ModelAdmin, TranslationAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == "package":
            kwargs["queryset"] = models.OpenBuffetPackage.objects.filter(
                restaurant__admin=request.user
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ("option", "package", "restaurant", "category")

    def restaurant(self, obj):
        return obj.package.restaurant

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(package__restaurant__admin=request.user)
