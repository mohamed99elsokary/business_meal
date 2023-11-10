from django.contrib import admin
from django.contrib.gis.db import models as db_models
from mapwidgets.widgets import GooglePointFieldWidget
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin, StackedInline

from . import models


@admin.register(models.Hotel)
class HotelAdmin(ModelAdmin, TranslationAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(admin=request.user)

    formfield_overrides = {db_models.PointField: {"widget": GooglePointFieldWidget}}


@admin.register(models.Hall)
class HallAdmin(ModelAdmin, TranslationAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(hotel__admin=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == "hotel":
            kwargs["queryset"] = models.Hotel.objects.filter(admin=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ("name", "hotel")


@admin.register(models.HallImages)
class HallImagesAdmin(ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(hotel__admin=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == "hotel":
            kwargs["queryset"] = models.Hotel.objects.filter(admin=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(models.HallOptions)
class HallOptionsAdmin(ModelAdmin, TranslationAdmin):
    "Admin View for HallOptions"
    list_display = ("hall", "option")


@admin.register(models.HallAvailableTime)
class HallAvailableTimeAdmin(ModelAdmin, TranslationAdmin):
    """Admin View for HallAvailableTime"""
