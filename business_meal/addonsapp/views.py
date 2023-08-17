from django.db.models import Q
from rest_framework import mixins, viewsets

from business_meal.addonsapp import models, serializers

""" PageSection """


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
