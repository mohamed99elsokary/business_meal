# Generated by Django 4.1.1 on 2023-11-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resturant_app", "0034_branch_estimated_mins"),
    ]

    operations = [
        migrations.AddField(
            model_name="meal",
            name="is_share_box",
            field=models.BooleanField(default=False),
        ),
    ]
