# Generated by Django 5.0.4 on 2024-07-11 22:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_product_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
