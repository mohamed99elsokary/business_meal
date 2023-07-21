from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

from . import models


@admin.register(models.Restaurant)
class RestaurantAdmin(ModelAdmin):
    """Admin View for Restaurant"""


@admin.register(models.Branch)
class BranchAdmin(ModelAdmin):
    """Admin View for Branch"""


@admin.register(models.Meal)
class MealAdmin(ModelAdmin):
    """Admin View for Meal"""


@admin.register(models.RestaurantOpenBuffet)
class RestaurantOpenBuffetAdmin(ModelAdmin):
    """Admin View for RestaurantOpenBuffet"""


@admin.register(models.Hotel)
class HotelAdmin(ModelAdmin):
    """Admin View for Hotel"""


@admin.register(models.HotelPlans)
class HotelPlansAdmin(ModelAdmin):
    """Admin View for HotelPlans"""


@admin.register(models.HotelImages)
class HotelImagesAdmin(ModelAdmin):
    """Admin View for HotelImages"""


@admin.register(models.UserFavorites)
class UserFavoritesAdmin(ModelAdmin):
    """Admin View for UserFavorites"""


@admin.register(models.Order)
class OrderAdmin(ModelAdmin):
    """Admin View for Order"""


@admin.register(models.OrderMeal)
class OrderMealAdmin(ModelAdmin):
    """Admin View for OrderMeal"""


@admin.register(models.MealOptions)
class MealOptionsAdmin(ModelAdmin):
    """Admin View for MealOptions"""
