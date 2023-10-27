from rest_framework import serializers

from . import models


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        exclude = ("user",)


class UpdateNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification

        fields = ("is_clicked", "is_action_taken")
