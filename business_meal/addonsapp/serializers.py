import random
import string

from rest_framework import serializers

from business_meal.addonsapp import models
from business_meal.services.custom_ModelSerializer import ErrorMixin

from ..hotel_app.serializers import HallOptions, HallOptionsSerializer
from ..openbuffet_app.serializers import (
    OpenBuffetPackageOptions,
    OpenBuffetPackageOptionsSerializer,
)
from ..resturant_app.serializers import MealOptions, MealOptionsSerializer

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
    options = serializers.SerializerMethodField()

    class Meta:
        model = models.OptionsCategory
        fields = "__all__"

    def get_options(self, obj) -> dict:
        query_prams = self.context["request"].GET

        if "hall" in query_prams:
            hall_options = HallOptions.objects.filter(
                category=obj, hall=query_prams["hall"]
            )
            return HallOptionsSerializer(hall_options, many=True).data

        elif "package" in query_prams:
            open_buffet_options = OpenBuffetPackageOptions.objects.filter(
                category=obj, package=query_prams["package"]
            )
            return OpenBuffetPackageOptionsSerializer(
                open_buffet_options, many=True
            ).data

        elif "meal" in query_prams:
            meal_options = MealOptions.objects.filter(
                category=obj, meal=query_prams["meal"]
            )
            return MealOptionsSerializer(meal_options, many=True).data

        else:
            return None


class LoyaltyPointsPromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoyaltyPointsPromoCode
        fields = "__all__"


class BuyPromoSerializer(serializers.Serializer):
    id = serializers.IntegerField(write_only=True)

    def generate_promo_code(self):
        code = "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(5)
        )
        while models.PromoCode.objects.filter(code=code).exists():
            code = "".join(
                random.choice(string.ascii_letters + string.digits) for _ in range(5)
            )
        return code

    def create(self, validated_data):
        user = self.context["request"].user
        promo = models.LoyaltyPointsPromoCode.objects.get(id=validated_data["id"])
        if user.loyalty_points < promo.price:
            raise serializers.ValidationError(
                {"detail": "sorry but you don't have enough loyalty points"}
            )
        user.loyalty_points -= promo.price
        user.save()
        code = models.PromoCode.objects.create(
            code=self.generate_promo_code(),
            times_to_use=1,
            discount=promo.discount,
            discount_type="amount",
        )
        return PromoCodeSerializer(code).data
