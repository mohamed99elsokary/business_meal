# Generated by Django 4.1.1 on 2023-08-15 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotel_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotel",
            name="rate",
            field=models.IntegerField(default=0),
        ),
    ]