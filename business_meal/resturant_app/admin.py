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


@admin.register(models.Category)
class CategoryAdmin(ModelAdmin):
    "Admin View for Category"
