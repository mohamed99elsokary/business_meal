# Generated by Django 4.1.1 on 2023-08-15 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resturant_app", "0027_remove_hall_hotel_remove_hallimages_hall_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="rate",
            field=models.IntegerField(default=0),
        ),
    ]
