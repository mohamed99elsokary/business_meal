from django.db import models
from django.db.models import Count, F, Q


class OpenBuffetPackageQuerySet(models.QuerySet):
    def admin_filter(self, user):
        return self.filter(restaurant__admin=user)
