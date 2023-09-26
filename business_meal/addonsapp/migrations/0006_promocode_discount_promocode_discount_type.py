# Generated by Django 4.1.1 on 2023-09-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("addonsapp", "0005_promocode_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="promocode",
            name="discount",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="promocode",
            name="discount_type",
            field=models.CharField(
                choices=[("amount", "amount"), ("discount", "discount")],
                default="amount",
                max_length=50,
            ),
        ),
    ]
