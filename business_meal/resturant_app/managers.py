from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.db import models


class BranchQuerySet(models.QuerySet):
    def get_user_location(self, location):
        location = location.split(",")
        lat = location[1]
        long = location[0]
        return Point(float(long), float(lat), srid=4326)

    def annotate_distance(self, location: str):
        user_location = self.get_user_location(location)
        return self.annotate(distance=Distance("location", user_location))
