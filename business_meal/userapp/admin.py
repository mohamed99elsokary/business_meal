from allauth.account.models import EmailAddress
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.gis.db import models as db_models
from django.utils.translation import gettext_lazy as _
from mapwidgets.widgets import GooglePointFieldWidget
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin, StackedInline
from unfold.decorators import display

from business_meal.userapp import models

from ..services.admin import UserAdmin as BaseUserAdmin
from . import models

admin.site.unregister(EmailAddress)
# admin.site.unregister(authtoken)


class AddressInline(StackedInline):
    model = models.Address
    min_num = 0
    extra = 0
    classes = ["collapse"]


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ["user", "id"]
    fieldsets = (
        (None, {"fields": ("username", "password", "is_development_api_user")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "email", "user_type")},
        ),
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

    @display(header=True)
    def user(self, obj):
        initials = (
            obj.first_name[0] + obj.last_name[0]
            if obj.first_name and obj.last_name
            else "BM"
        )
        return obj.email, f"{obj.first_name} {obj.last_name}", initials


""" Address """


@admin.register(models.Address)
class AddressAdmin(ModelAdmin):
    list_display = ["id", "user", "postal_code"]
    list_select_related = ("user",)
    autocomplete_fields = ["user"]
    search_fields = ("user__email", "user__username")

    formfield_overrides = {db_models.PointField: {"widget": GooglePointFieldWidget}}


@admin.register(models.DeliveryCar)
class DeliveryCarAdmin(ModelAdmin, TranslationAdmin):
    """Admin View for DeliveryCar"""


@admin.register(models.UserFavorites)
class UserFavoritesAdmin(ModelAdmin):
    """Admin View for UserFavorites"""
