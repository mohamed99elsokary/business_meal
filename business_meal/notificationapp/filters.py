from django_filters import rest_framework as filters

from . import models


class NotificationFilter(filters.FilterSet):
    class Meta:
        model = models.Notification
        fields = [
            "is_seen",
        ]
