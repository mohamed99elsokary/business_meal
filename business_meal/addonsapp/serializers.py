from rest_framework import serializers

from business_meal.addonsapp import models
from business_meal.services.custom_ModelSerializer import ErrorMixin

""" PageSection """


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = "__all__"


class TermsAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TermsAndConditions
        fields = "__all__"


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrivacyPolicy
        fields = "__all__"


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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PromoCode
        fields = "__all__"


class OptionsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OptionsCategory
        fields = "__all__"
