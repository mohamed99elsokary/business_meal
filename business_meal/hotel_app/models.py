from django.db import models

from business_meal.userapp.models import User


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
        return self.hotel.name


class HallOptions(models.Model):
    # relations
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
        return self.nameuser_address
