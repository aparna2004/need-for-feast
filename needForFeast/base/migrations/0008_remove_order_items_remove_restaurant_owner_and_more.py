# Generated by Django 4.2.6 on 2023-11-01 14:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0007_items_rating_restaurant_image_restaurant_rating_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="items",
        ),
        migrations.RemoveField(
            model_name="restaurant",
            name="owner",
        ),
        migrations.DeleteModel(
            name="CustomerDelivererRelationship",
        ),
        migrations.DeleteModel(
            name="Items",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="Restaurant",
        ),
    ]
