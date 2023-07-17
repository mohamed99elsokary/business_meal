from rest_framework import mixins, viewsets

from business_meal.addonsapp.models import ContactUs, PageSection
from business_meal.addonsapp.serializers import (
    ContactUsSerializer,
    PageSectionSerializer,
)

""" PageSection """


class PageSectionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PageSectionSerializer
    queryset = PageSection.objects.all()
    pagination_class = None
    filterset_fields = ("page_type",)


""" Contact us """


class ContactUsViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactUs.objects
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        serializer.save()
        # serializer.instance.send_notification_email()
