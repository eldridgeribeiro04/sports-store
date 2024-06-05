# Generated by Django 5.0.4 on 2024-06-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_alter_item_brand_alter_item_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female"), ("unisex", "Unisex")],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="size",
            field=models.CharField(
                choices=[
                    ("s", "S"),
                    ("l", "L"),
                    ("xxxl", "XXXL"),
                    ("xl", "XL"),
                    ("3xl", "3XL"),
                    ("xxl", "XXL"),
                    ("xs", "XS"),
                    ("4xl", "4XL"),
                    ("m", "M"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="item",
            unique_together={("name", "brand", "category")},
        ),
    ]