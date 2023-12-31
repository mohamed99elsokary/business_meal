from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

from . import models


@admin.register(models.Hotel)
class HotelAdmin(ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(admin=request.user)


@admin.register(models.Hall)
class HallAdmin(ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(hotel__admin=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == "hotel":
            kwargs["queryset"] = models.Hotel.objects.filter(admin=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


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
class HallOptionsAdmin(ModelAdmin):
    "Admin View for HallOptions"
