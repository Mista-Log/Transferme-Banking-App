import random
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


class OTPVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="otp_verification")
    phone_number = models.CharField(max_length=15, unique=True)
    otp_code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        """Generate a 5-digit OTP"""
        self.otp_code = str(random.randint(10000, 99999))
        self.save()
        return self.otp_code

    def is_valid(self):
        """Check if OTP is still valid (e.g., within 5 minutes)"""
        from django.utils.timezone import now
        return (now() - self.created_at).seconds < 300  # 5 minutes
