# Generated by Django 5.0.4 on 2024-07-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myuser",
            name="email",
            field=models.EmailField(max_length=100, unique=True, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="myuser",
            name="username",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Username"
            ),
        ),
    ]