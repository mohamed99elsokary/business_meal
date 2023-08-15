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
