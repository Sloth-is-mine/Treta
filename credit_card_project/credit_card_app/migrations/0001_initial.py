# Generated by Django 5.0.1 on 2024-01-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserCreditCard",
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
                ("username", models.CharField(max_length=225)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("encrypted_credit_card", models.TextField()),
            ],
        ),
    ]
