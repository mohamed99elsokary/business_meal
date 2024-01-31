from bit68_notifications.models import BulkNotification, ExpoDevice
from django.db import models

from ..userapp.models import User


class Notification(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # fields
    title = models.TextField()
    description = models.TextField()
    is_seen = models.BooleanField(default=False)
    is_clicked = models.BooleanField(default=False)
    is_action_taken = models.BooleanField(default=False)
    body = models.JSONField(default=None, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, null=True, blank=True)


class UpdatedExpoDevice(ExpoDevice):
    type = models.CharField(
        max_length=50, choices=[("driver", "driver"), ("customer", "customer")]
    )

    def __str__(self):
        return self.name


class UpdatedBulkNotification(BulkNotification):
    user_type = models.CharField(
        max_length=50, choices=[("driver", "driver"), ("customer", "customer")]
    )

    def send_expo(self):
        handler = UpdatedExpoDevice.objects.filter(type=self.user_type).send_message(
            self.title, self.body
        )

        if not handler:
            return

        self.response_log = handler.log
        self.is_successful = not handler.is_failed_request
        string = "\n" + "*" * 50 + "\n"
        self.failed_tokens = string.join(handler.failed_tokens)
