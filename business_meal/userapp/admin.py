from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin, StackedInline

from business_meal.userapp import models

from . import models


class AddressInline(StackedInline):
    model = models.Address
    min_num = 0
    extra = 0
    classes = ["collapse"]


@admin.register(models.User)
class UserAdmin(ModelAdmin, BaseUserAdmin):
    list_display = [
        "id",
        "email",
        "first_name",
        "last_name",
    ]
    fieldsets = (
        (None, {"fields": ("username", "password", "is_development_api_user")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


""" Address """


@admin.register(models.Address)
class AddressAdmin(ModelAdmin):
    list_display = ["id", "user", "postal_code"]
    list_select_related = ("user",)
    autocomplete_fields = ["user"]
    search_fields = ("user__email", "user__username")


@admin.register(models.DeliveryCar)
class DeliveryCarAdmin(ModelAdmin):
    """Admin View for DeliveryCar"""
