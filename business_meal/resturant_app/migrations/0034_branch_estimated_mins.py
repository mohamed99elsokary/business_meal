# Generated by Django 4.1.1 on 2023-11-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resturant_app", "0033_branch_delivery_fees"),
    ]

    operations = [
        migrations.AddField(
            model_name="branch",
            name="estimated_mins",
            field=models.FloatField(default=0),
        ),
    ]