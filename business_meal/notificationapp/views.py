from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import NotificationFilter
from .models import Notification
from .serializers import NotificationSerializer, UpdateNotificationSerializer


# Create your views here.
class NotificationsViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filterset_class = NotificationFilter
    ordering = ("-id",)

    def get_serializer_class(self):
        if self.action in {"update", "partial_update"}:
            return UpdateNotificationSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    @action(methods=["get"], detail=False, url_path="make_all_notification_seen")
    def make_all_notification_seen(self, request):
        Notification.objects.filter(user=self.request.user).update(is_seen=True)
        return Response("done")
