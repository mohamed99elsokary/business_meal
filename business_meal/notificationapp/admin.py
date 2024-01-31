from bit68_notifications.models import BulkNotification, ExpoDevice
from django.contrib import admin
from unfold.admin import ModelAdmin

from . import models

admin.site.unregister(ExpoDevice)

admin.site.unregister(BulkNotification)


@admin.register(models.Notification)
class NotificationAdmin(ModelAdmin):
    """Admin View for Notification"""


@admin.register(models.UpdatedBulkNotification)
class BulkNotificationAdmin(ModelAdmin):
    """Admin View for BulkNotification"""


@admin.register(models.UpdatedExpoDevice)
class ExpoDeviceAdmin(ModelAdmin):
    """Admin View for ExpoDevice"""
