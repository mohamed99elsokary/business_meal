# Generated by Django 4.1.1 on 2023-07-21 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("resturant_app", "0011_rename_ordermeal_orderitem_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderitemoption",
            name="option",
        ),
        migrations.AddField(
            model_name="order",
            name="promo",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="resturant_app.promocode",
            ),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="package",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="resturant_app.restaurantopenbuffetpackage",
            ),
        ),
        migrations.AddField(
            model_name="orderitemoption",
            name="meal_option",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="resturant_app.mealoptions",
            ),
        ),
        migrations.AddField(
            model_name="orderitemoption",
            name="package_option",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="resturant_app.openbuffetpackageoptions",
            ),
        ),
    ]