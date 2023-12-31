# Generated by Django 4.1.1 on 2023-08-15 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("openbuffet_app", "0001_initial"),
        ("resturant_app", "0027_remove_hall_hotel_remove_hallimages_hall_and_more"),
        ("hotel_app", "0001_initial"),
        ("addonsapp", "0004_category_image_promocode"),
        ("userapp", "0003_userfavorites"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("preparing", "preparing"),
                            ("delivering", "delivering"),
                            ("delivered", "delivered"),
                            ("canceled", "canceled"),
                            ("is_paid", "is_paid"),
                        ],
                        max_length=50,
                    ),
                ),
                ("payment_type", models.CharField(max_length=50)),
                ("is_checkout", models.BooleanField()),
                ("is_paid", models.BooleanField(default=False)),
                ("payment_url", models.CharField(max_length=50)),
                ("note", models.CharField(max_length=50)),
                ("ordered_time", models.DateTimeField()),
                ("scheduled_time", models.DateTimeField()),
                ("estimated_time", models.DateTimeField()),
                ("delivered_time", models.DateTimeField()),
                (
                    "delivery_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="delivery_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "promo",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="addonsapp.promocode",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userapp.address",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItemOption",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "meal_option",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resturant_app.mealoptions",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="order_app.order",
                    ),
                ),
                (
                    "package_option",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="openbuffet_app.openbuffetpackageoptions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("note", models.CharField(max_length=50)),
                (
                    "hall",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hotel_app.hall",
                    ),
                ),
                (
                    "meal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resturant_app.meal",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="order_app.order",
                    ),
                ),
                (
                    "package",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="openbuffet_app.openbuffetpackage",
                    ),
                ),
            ],
        ),
    ]
