from rest_framework import serializers

from . import models


class OpenBuffetPackageSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = models.OpenBuffetPackage
        fields = "__all__"

    def get_category_name(self, obj):
        return obj.category.name


class OpenBuffetPackageOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OpenBuffetPackageOptions
        fields = "__all__"
