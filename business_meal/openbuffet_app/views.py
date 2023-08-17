from rest_framework import viewsets

from . import filters, models, serializers


class OpenBuffetPackageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = query = models.OpenBuffetPackage.objects.all().select_related("category")
    serializer_class = serializers.OpenBuffetPackageSerializer
    pagination_class = None
    filterset_fields = ["restaurant"]


class OpenBuffetOptionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = query = models.OpenBuffetPackageOptions.objects.all()
    serializer_class = serializers.OpenBuffetPackageOptionsSerializer
    filterset_fields = ["is_additional"]
