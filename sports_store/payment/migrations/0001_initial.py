# Generated by Django 5.0.4 on 2024-07-30 23:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("shop_cart", "0003_cart_paid"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_charge_id", models.CharField(max_length=255)),
                ("amount", models.PositiveIntegerField()),
                ("paid_at", models.DateTimeField(auto_now_add=True)),
                (
                    "cart",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="shop_cart.cart"
                    ),
                ),
            ],
        ),
    ]
