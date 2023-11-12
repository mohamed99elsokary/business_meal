from rest_framework import serializers

from . import models


class TinyRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ("id", "name", "phone")


class RestaurantSerializer(serializers.ModelSerializer):
    lowest_meal_price = serializers.SerializerMethodField()

    class Meta:
        model = models.Restaurant
        fields = "__all__"

    def get_lowest_meal_price(self, obj) -> int:
        if meals := models.Meal.objects.filter(restaurant=obj):
            return meals.order_by("price").first().price
        return None


class MealSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Meal
        fields = "__all__"

    def get_category_name(self, obj) -> str:
        return obj.category.name


class MealOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MealOptions
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    location = serializers.ListField()
    distance = serializers.CharField(default=None)

    class Meta:
        model = models.Branch
        fields = "__all__"
