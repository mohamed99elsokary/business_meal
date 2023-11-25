from django.contrib import admin
from django.db.models import Q
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RangeDateFilter

from . import models


@admin.register(models.Order)
class OrderAdmin(ModelAdmin, ImportExportModelAdmin):
    list_filter = (
        "is_checkout",
        "is_paid",
        "status",
        "payment_type",
        ("ordered_time", RangeDateFilter),
    )
    list_filter_submit = True
    list_display = (
        "id",
        "restaurant",
        "branch",
        "hotel",
        "status",
        "total",
        "payment_type",
        "ordered_time",
        "is_checkout",
        "is_paid",
    )
    search_fields = ("id",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(
            Q(Q(restaurant__admin=request.user) | Q(hotel__admin=request.user))
        )


@admin.register(models.OrderItem)
class OrderItemAdmin(ModelAdmin):
    """Admin View for OrderMeal"""

    list_display = ("id", "order_id")


@admin.register(models.PromoCode)
class PromoCodeAdmin(ModelAdmin):
    """Admin View for PromoCode"""


@admin.register(models.OrderItemOption)
class OrderItemOptionAdmin(ModelAdmin):
    """Admin View for OrderItemOption"""
