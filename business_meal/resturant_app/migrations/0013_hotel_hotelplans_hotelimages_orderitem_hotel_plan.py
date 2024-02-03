# Generated by Django 4.1.1 on 2023-07-21 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("resturant_app", "0012_remove_orderitemoption_option_order_promo_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hotel",
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
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="HotelPlans",
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
                ("number_of_guests", models.IntegerField()),
                ("price", models.IntegerField()),
                ("services", models.CharField(max_length=50)),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resturant_app.hotel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HotelImages",
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
                ("image", models.ImageField(upload_to="media/")),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resturant_app.hotel",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="orderitem",
            name="hotel_plan",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="resturant_app.hotelplans",
            ),
        ),
    ]