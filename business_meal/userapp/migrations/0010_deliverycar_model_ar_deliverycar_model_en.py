# Generated by Django 4.1.1 on 2023-11-02 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0009_user_user_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="deliverycar",
            name="model_ar",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="deliverycar",
            name="model_en",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
