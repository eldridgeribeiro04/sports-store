# Generated by Django 5.0.4 on 2024-07-11 22:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_alter_product_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default=1, null=True),
        ),
    ]
