from rest_framework import serializers

from .models import OpenBuffetPackage, OpenBuffetPackageOptions


class OpenBuffetPackageSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = OpenBuffetPackage
        fields = "__all__"

    def get_category_name(self, obj):
        return obj.category.name


class OpenBuffetPackageOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenBuffetPackageOptions
        fields = "__all__"
