# Generated by Django 4.1.1 on 2023-09-22 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order_app", "0006_order_hotel_order_restaurant_alter_order_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="payment_type",
        ),
        migrations.RemoveField(
            model_name="order",
            name="type",
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_url",
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
