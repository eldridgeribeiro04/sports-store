# Generated by Django 5.0.4 on 2024-04-26 23:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0009_alter_category_brand"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gender",
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
                (
                    "gender_type",
                    models.CharField(default="Not assigned", max_length=255),
                ),
            ],
        ),
        migrations.AddField(
            model_name="category",
            name="gender",
            field=models.ForeignKey(
                default="0",
                on_delete=django.db.models.deletion.CASCADE,
                to="product.gender",
            ),
            preserve_default=False,
        ),
    ]