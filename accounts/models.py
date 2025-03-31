from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=5, default="USD")

    def __str__(self):
        return f"{self.user.username} - {self.currency} {self.balance}"


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wallet")
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} - ${self.balance}"
    

BANK_CHOICES = [
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
]

class Bank(models.Model):
    name = models.CharField(max_length=50, choices=BANK_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()
