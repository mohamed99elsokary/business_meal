from rest_framework import serializers

from . import models


class HotelSerializer(serializers.ModelSerializer):
    min_cap = serializers.SerializerMethodField()
    max_cap = serializers.SerializerMethodField()

    class Meta:
        model = models.Hotel
        fields = "__all__"

    def get_min_cap(self, obj) -> int:
        return obj.hall_set.order_by("min").first().min if obj.hall_set.count() else 0

    def get_max_cap(self, obj) -> int:
        return obj.hall_set.order_by("-max").first().max if obj.hall_set.count() else 0


class HallImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HallImages
        fields = "__all__"


class HotelHallSerializer(serializers.ModelSerializer):
    # category_name = serializers.SerializerMethodField()
    images = HallImagesSerializer(source="hallimages_set", many=True)

    class Meta:
        model = models.Hall
        fields = "__all__"

    # def get_category_name(self, obj) -> str:
    #     return obj.category.name


class HallOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HallOptions
        fields = "__all__"
