# Generated by Django 4.1.1 on 2023-07-06 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("userapp", "0002_remove_address_description_address_apartment_and_more"),
        ("resturant_app", "0001_initial"),
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
                            ("canceled", "canceled"),
                            ("returned", "returned"),
                            ("delivering", "delivering"),
                            ("preparing", "preparing"),
                            ("delivered", "delivered"),
                        ],
                        max_length=50,
                    ),
                ),
                ("payment_type", models.CharField(max_length=50)),
                ("is_checkout", models.BooleanField()),
                ("is_paid", models.BooleanField()),
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
            name="UserFavorites",
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
                    "meal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resturant_app.meal",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderMeal",
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
                        to="resturant_app.order",
                    ),
                ),
            ],
        ),
    ]