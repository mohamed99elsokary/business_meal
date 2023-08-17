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
