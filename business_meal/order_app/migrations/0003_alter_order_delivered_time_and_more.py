# Generated by Django 4.1.1 on 2023-09-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order_app", "0002_alter_orderitem_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="delivered_time",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="estimated_time",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="ordered_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="scheduled_time",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    (1, "Pending Payment"),
                    (2, "Pending Confirmation"),
                    (3, "Confirmed"),
                    (4, "Preparing"),
                    (5, "Delivering"),
                    (6, "Delivered"),
                    (7, "Ready For Pickup"),
                    (8, "Cancelled"),
                ],
                max_length=50,
            ),
        ),
    ]
