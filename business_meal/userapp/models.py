from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.gis.db import models as gis_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from business_meal.services.custom_Models import CustomModel
from business_meal.services.helpers import rand_int_4digits
from business_meal.userapp.model_mixins import UserMixin


class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields["is_active"] = True
        return super().create_superuser(username, email, password, **extra_fields)


class User(UserMixin, CustomModel, AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        unique=True,
    )
    username = models.CharField(
        _("username"),
        max_length=150,
    )
    phone = models.CharField(_("Phone"), max_length=50, null=True, blank=True)

    # verification
    is_active = models.BooleanField(default=True)
    is_new = models.BooleanField(default=True)

    verification_code = models.CharField(
        max_length=10, default=rand_int_4digits, null=True, blank=True
    )
    is_deleted = models.BooleanField(default=False)
    is_development_api_user = models.BooleanField(
        default=False,
        help_text=_(
            "indicate if this user could be used in developer "
            "only private APIs like create statistics endpoints."
        ),
    )
    password_reset_code = models.CharField(max_length=10, null=True, blank=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Address(models.Model):
    user = models.ForeignKey("User", verbose_name=_("User"), on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    location = gis_model.PointField(srid=4326, blank=True, null=True)
    is_default = models.BooleanField(_("Is default"), default=False)
    postal_code = models.CharField(_("Postal code"), max_length=100)
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    floor = models.CharField(max_length=50)
    apartment = models.CharField(max_length=50)
    name = models.CharField(max_length=50, default=None, null=True, blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.user}"

    class Meta:
        verbose_name_plural = "Addresses"


class DeliveryCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    plat = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user} {self.model} {self.plat}"


class UserFavorites(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey("resturant_app.Meal", on_delete=models.CASCADE)

    def __str__(self):
        return self.user
