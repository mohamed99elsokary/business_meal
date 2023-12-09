from django.contrib.gis.db import models as gis_model
from django.db import models

from business_meal.userapp.models import User

from ..addonsapp.models import OptionsCategory
from .managers import HotelQuerySet


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/", null=True, blank=True, default=None)
    cover_photo = models.ImageField(
        upload_to="media/", null=True, blank=True, default=None
    )
    description = models.TextField()
    address = models.CharField(max_length=50)
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    rate = models.IntegerField(default=0)
    location = gis_model.PointField(srid=4326, blank=True, null=True)
    objects: HotelQuerySet = HotelQuerySet.as_manager()

    def __str__(self):
        return self.name


class Hall(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    min = models.IntegerField(help_text="number of guests", default=0)
    max = models.IntegerField(help_text="number of guests", default=0)
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.hotel.name}"


class HallAvailableTime(models.Model):
    # relations
    Hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=50)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.pk)


class HallBusyDate(models.Model):
    # relations
    Hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    # fields
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.pk)


class HallOptions(models.Model):
    # relations
    category = models.ForeignKey(
        OptionsCategory, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    # fields
    option = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.option


class HallImages(models.Model):
    # relations
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    # fields
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.hall.name
