# Generated by Django 4.2.6 on 2023-11-01 10:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0006_items_customer_deliverer_owner_restaurant_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="items",
            name="rating",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=3,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(5.0),
                ],
            ),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="image",
            field=models.ImageField(null=True, upload_to="images/restaurant"),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="rating",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=3,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(5.0),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="items",
            name="quantity",
            field=models.PositiveIntegerField(
                null=True, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
