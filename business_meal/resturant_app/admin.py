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
class OrderItemOptionAdmin(ModelAdmin):
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


@admin.register(models.OpenBuffetPackage)
class OpenBuffetPackage(ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(restaurant__admin=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser and db_field.name == "restaurant":
            kwargs["queryset"] = models.Restaurant.objects.filter(
                admin=request.user, is_open_buffet=True
            )
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
            kwargs["queryset"] = models.OpenBuffetPackage.objects.filter(
                restaurant__admin=request.user
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


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


@admin.register(models.Category)
class CategoryAdmin(ModelAdmin):
    "Admin View for Category"


@admin.register(models.HallOptions)
class HallOptionsAdmin(ModelAdmin):
    "Admin View for HallOptions"
