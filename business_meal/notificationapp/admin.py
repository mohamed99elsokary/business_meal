from django.contrib import admin
from unfold.admin import ModelAdmin

from . import models


@admin.register(models.Notification)
class NotificationAdmin(ModelAdmin):
    """Admin View for Notification"""
