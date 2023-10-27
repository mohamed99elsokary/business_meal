from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NotificationappConfig(AppConfig):
    name = "business_meal.notificationapp"
    verbose_name = _("Notificationapp")
