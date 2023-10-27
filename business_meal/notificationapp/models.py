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
