# Generated by Django 4.1.1 on 2023-07-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resturant_app", "0024_hotel_cover_photo_restaurant_cover_photo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hall",
            name="number_of_guests",
        ),
        migrations.AddField(
            model_name="hall",
            name="max",
            field=models.IntegerField(default=0, help_text="number of guests"),
        ),
        migrations.AddField(
            model_name="hall",
            name="min",
            field=models.IntegerField(default=0, help_text="number of guests"),
        ),
    ]
