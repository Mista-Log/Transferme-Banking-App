# Generated by Django 5.1.3 on 2025-03-27 22:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0002_remove_transaction_receiver_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentTransaction",
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
                    "category",
                    models.CharField(
                        choices=[
                            ("electricity", "Electricity"),
                            ("ecommerce", "E-Commerce"),
                            ("transport", "Transportation"),
                            ("mobile_data", "Mobile & Data"),
                            ("internet", "TV & Internet"),
                            ("pharmacy", "Pharmacy"),
                            ("tickets", "Tickets"),
                            ("hotel", "Hotel"),
                            ("flight", "Flight"),
                            ("fuel", "Fuel"),
                            ("gaming", "Pay Google Play"),
                            ("food", "Food & Drink"),
                        ],
                        max_length=20,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
