# Generated by Django 5.1.3 on 2025-03-31 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_wallet"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bank",
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
                    "name",
                    models.CharField(
                        choices=[
                            ("mcb", "MCB"),
                            ("alalah", "Alalah"),
                            ("soneri", "Soneri"),
                            ("bop", "BOP"),
                            ("hbl", "HBL"),
                            ("ubl", "UBL"),
                            ("jazzcash", "JazzCash"),
                            ("easypaisa", "EasyPaisa"),
                            ("mobicash", "MobiCash"),
                            ("payoneer", "Payoneer"),
                            ("paypal", "PayPal"),
                            ("stripe", "Stripe"),
                        ],
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
