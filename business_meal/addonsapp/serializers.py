from rest_framework import serializers

from business_meal.addonsapp import models
from business_meal.services.custom_ModelSerializer import ErrorMixin

""" PageSection """


class SliderPictureSerializer(ErrorMixin, serializers.ModelSerializer):
    class Meta:
        model = models.SliderPicture
        fields = "__all__"


class SectionContentSerializer(ErrorMixin, serializers.ModelSerializer):
    class Meta:
        model = models.SectionContent
        fields = "__all__"


class PageSectionSerializer(ErrorMixin, serializers.ModelSerializer):
    sectioncontent_set = SectionContentSerializer(many=True)
    sliderpicture_set = SliderPictureSerializer(many=True)

    class Meta:
        model = models.PageSection
        fields = "__all__"


""" Contact us """


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = "__all__"


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ads
        fields = "__all__"
