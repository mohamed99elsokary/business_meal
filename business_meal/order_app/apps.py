from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrderAppConfig(AppConfig):
    name = "business_meal.order_app"
    verbose_name = _("OrderApp")
