# Generated by Django 4.1.1 on 2023-08-15 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resturant_app", "0028_restaurant_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="meal",
            name="is_top_dish",
            field=models.BooleanField(default=False),
        ),
    ]
