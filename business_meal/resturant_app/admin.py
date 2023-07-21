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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(restaurant__admin=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == "restaurant":
            kwargs["queryset"] = models.Restaurant.objects.filter(admin=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(models.UserFavorites)
class UserFavoritesAdmin(ModelAdmin):
    """Admin View for UserFavorites"""


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
class OrderItemOptionAdmin(admin.ModelAdmin):
    """Admin View for OrderItemOption"""


@admin.register(models.MealOptions)
class MealOptionsAdmin(ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(meal__restaurant__admin=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == "meal":
            kwargs["queryset"] = models.Meal.objects.filter(
                restaurant__admin=request.user
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(models.RestaurantOpenBuffetPackage)
class RestaurantOpenBuffetPackageAdmin(ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(restaurant__admin=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == "restaurant":
            kwargs["queryset"] = models.Restaurant.objects.filter(admin=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(models.OpenBuffetPackageOptions)
class OpenBuffetPackageOptionsAdmin(ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(package__restaurant__admin=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == "package":
            kwargs["queryset"] = models.RestaurantOpenBuffetPackage.objects.filter(
                restaurant__admin=request.user
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# @admin.register(models.Hotel)
# class HotelAdmin(ModelAdmin):
#     """Admin View for Hotel"""


# @admin.register(models.HotelPlans)
# class HotelPlansAdmin(ModelAdmin):
#     """Admin View for HotelPlans"""


# @admin.register(models.HotelImages)
# class HotelImagesAdmin(ModelAdmin):
#     """Admin View for HotelImages"""
