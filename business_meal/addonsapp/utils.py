from bit68_notifications.models import ExpoDevice

from ..notificationapp.models import Notification


class NotificationHandler:
    def __init__(
        self,
        users: list,
        title: str,
        body: str,
        is_in_app: bool = False,
        is_push_notification: bool = False,
        extra: dict = None,
    ):
        self.users = users
        self.devices = ExpoDevice.objects.filter(user__in=users)
        self.title = title
        self.body = body
        self.extra = extra
        if is_push_notification:
            self.push_notifications()
        if is_in_app:
            self.in_app_notifications()
        return

    def in_app_notifications(self):
        return Notification.objects.bulk_create(
            [
                Notification(
                    title=self.title, description=self.body, user=user, body=self.extra
                )
                for user in self.users
            ]
        )

    def push_notifications(self):
        devices = self.devices.distinct("registration_id")
        return devices.send_message(title=self.title, body=self.body, extra=self.extra)
