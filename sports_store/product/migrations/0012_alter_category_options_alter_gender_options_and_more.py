# Generated by Django 5.0.4 on 2024-04-27 03:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0011_alter_brand_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="gender",
            options={"verbose_name": "Gender", "verbose_name_plural": "Genders"},
        ),
        migrations.AlterModelOptions(
            name="item",
            options={"verbose_name": "Item", "verbose_name_plural": "Items"},
        ),
    ]
