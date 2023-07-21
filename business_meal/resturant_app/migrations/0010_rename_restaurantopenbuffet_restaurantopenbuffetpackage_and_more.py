# Generated by Django 4.1.1 on 2023-07-21 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("resturant_app", "0009_restaurantopenbuffet"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="RestaurantOpenBuffet",
            new_name="RestaurantOpenBuffetPackage",
        ),
        migrations.CreateModel(
            name="OpenBuffetPackageOptions",
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
                ("option", models.CharField(max_length=50)),
                ("is_additional", models.BooleanField(default=False)),
                (
                    "package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resturant_app.restaurantopenbuffetpackage",
                    ),
                ),
            ],
        ),
    ]
