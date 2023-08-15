from rest_framework import viewsets

from . import filters, models, serializers

# Create your views here.


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.DetailedOrderSerializer
        return super().get_serializer_class()
