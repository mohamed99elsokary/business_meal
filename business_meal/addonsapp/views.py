from django.db.models import Q
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..services.views import ModelViewSetClones
from . import filters, models, serializers

""" PageSection """


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer


class TermsAndConditionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TermsAndConditions.objects.all()
    serializer_class = serializers.TermsAndConditionsSerializer


class PrivacyPolicyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.PrivacyPolicy.objects.all()
    serializer_class = serializers.PrivacyPolicySerializer


class PageSectionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.PageSectionSerializer
    queryset = models.PageSection.objects.all()
    pagination_class = None
    filterset_fields = ("page_type",)


""" Contact us """


class ContactUsViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.ContactUs.objects
    serializer_class = serializers.ContactUsSerializer

    def perform_create(self, serializer):
        serializer.save()
        # serializer.instance.send_notification_email()


class AdsViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Ads.objects.all()
    serializer_class = serializers.AdsSerializer


class CategoryViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class PromoCodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.PromoCode.objects.filter(is_active=True)
    serializer_class = serializers.PromoCodeSerializer
    lookup_field = "code"

    def get_queryset(self):
        return self.queryset.filter(Q(user=self.request.user) | Q(user__isnull=True))


class OptionsCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.OptionsCategory.objects.all()
    serializer_class = serializers.OptionsCategorySerializer
    filterset_class = filters.OptionsCategoryFilter


class LoyaltyPointsPromoCodeViewSet(viewsets.ReadOnlyModelViewSet, ModelViewSetClones):
    queryset = models.LoyaltyPointsPromoCode.objects.all()
    serializer_class = serializers.LoyaltyPointsPromoCodeSerializer

    def get_serializer_class(self):
        if self.action == "buy_promo":
            return serializers.BuyPromoSerializer
        return super().get_serializer_class()

    @action(methods=["post"], detail=False)
    def buy_promo(self, request, *args, **kwargs):
        return super().create_clone(request, data=False, *args, **kwargs)
