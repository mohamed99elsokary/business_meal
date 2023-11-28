from django.db.models import F
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from ..order_app.models import OrderItem
from . import models, serializers,filters


class HotelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Hotel.objects.all().prefetch_related("hall_set")
    serializer_class = serializers.HotelSerializer
    filterset_class = filters.HotelFilter

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


class UnavailableHallDatesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.HallBusyDate.objects.all()
    serializer_class = serializers.UnavailableHallDatesSerializer
    filterset_fields = ["Hall"]

    def list(self, request, *args, **kwargs):
        hall = request.GET.get("Hall")

        busy_dates = models.HallBusyDate.objects.filter(
            Hall=hall, date__gte=timezone.now()
        ).values_list("date", flat=True)
        taken_dates = (
            OrderItem.objects.annotate(date=F("order__scheduled_time"))
            .filter(hall=hall, date__gte=timezone.now())
            .values_list("date", flat=True)
        )
        dates = list(busy_dates) + list(taken_dates)
        return Response(dates)
