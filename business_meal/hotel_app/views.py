from rest_framework import viewsets

from . import models, serializers


class HotelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Hotel.objects.all().prefetch_related("hall_set")
    serializer_class = serializers.HotelSerializer


class HotelHallViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (
        models.Hall.objects.all().prefetch_related("hallimages_set")
        # .select_related("category")
    )
    serializer_class = serializers.HotelHallSerializer
    pagination_class = None
    filterset_fields = ["hotel"]


class HallOptionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.HallOptions.objects.all()
    serializer_class = serializers.HallOptionsSerializer
    pagination_class = None
    filterset_fields = ["hall"]
