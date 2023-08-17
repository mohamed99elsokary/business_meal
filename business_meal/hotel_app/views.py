from rest_framework import viewsets

from . import models, serializers


class HotelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Hotel.objects.all().prefetch_related("hall_set")
    serializer_class = serializers.HotelSerializer
