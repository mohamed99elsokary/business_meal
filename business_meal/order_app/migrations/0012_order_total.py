# Generated by Django 4.1.1 on 2023-10-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order_app", "0011_remove_orderitemoption_order_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total",
            field=models.IntegerField(default=0),
        ),
    ]
