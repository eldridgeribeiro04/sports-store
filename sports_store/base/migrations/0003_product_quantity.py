# Generated by Django 5.0.4 on 2024-07-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_category_alter_brand_brand_name_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default=None, null=True),
        ),
    ]
