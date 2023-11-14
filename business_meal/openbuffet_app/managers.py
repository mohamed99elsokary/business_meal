from django.db import models


class OpenBuffetPackageQuerySet(models.QuerySet):
    def admin_filter(self, user):
        return self.filter(restaurant__admin=user)


class OpenBuffetPackageOptionsQuerySet(models.QuerySet):
    def admin_filter(self, user):
        return self.filter(package__restaurant__admin=user)
