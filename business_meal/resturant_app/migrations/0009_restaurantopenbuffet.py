# Generated by Django 4.1.1 on 2023-07-21 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("resturant_app", "0008_order_is_paid"),
    ]

    operations = [
        migrations.CreateModel(
            name="RestaurantOpenBuffet",
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
                ("clients_count", models.IntegerField()),
                ("image", models.ImageField(upload_to="")),
                ("price", models.IntegerField()),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resturant_app.restaurant",
                    ),
                ),
            ],
        ),
    ]