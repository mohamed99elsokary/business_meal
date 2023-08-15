from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

from . import models


@admin.register(models.Order)
class OrderAdmin(ModelAdmin):
    """Admin View for Order"""


@admin.register(models.OrderItem)
class OrderItemAdmin(ModelAdmin):
    """Admin View for OrderMeal"""


@admin.register(models.PromoCode)
class PromoCodeAdmin(ModelAdmin):
    """Admin View for PromoCode"""


@admin.register(models.OrderItemOption)
class OrderItemOptionAdmin(ModelAdmin):
    """Admin View for OrderItemOption"""
