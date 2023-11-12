# Generated by Django 4.1.1 on 2023-11-12 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hotel_app", "0008_hallavailabletime_name_ar_hallavailabletime_name_en"),
        ("order_app", "0021_order_branch"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitemoption",
            name="hall_option",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hotel_app.halloptions",
            ),
        ),
    ]
