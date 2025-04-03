from django.db import models
from django.contrib.auth import get_user_model
from cards.models import Card
from accounts.models import Bank
from notifications.utils import send_notification


User = get_user_model()

TRANSACTION_TYPES = (
    ("credit", "Credit"),
    ("debit", "Debit"),
    ("cashback", "Cashback"),
)
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True, related_name="transactions")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} {self.amount}"


TRANSACTION_CATEGORIES = (
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
)
class PaymentTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    category = models.CharField(max_length=20, choices=TRANSACTION_CATEGORIES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} ${self.amount}"
    


class MoneyTransfer(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_transfers")
    receiver_account_number = models.CharField(max_length=20)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} to {self.receiver_account_number} - ${self.amount}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Automatically send a notification after saving
        send_notification(self.sender, f"Transfer of ${self.amount} to {self.receiver_account_number} successful.")


SIM_PROVIDERS = [
    ('jazz', 'Jazz'),
    ('telenor', 'Telenor'),
    ('zong', 'Zong'),
    ('ufone', 'Ufone'),
]

class SIMTopUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sim_topups")
    phone_number = models.CharField(max_length=15)
    provider = models.CharField(max_length=20, choices=SIM_PROVIDERS)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Top-up {self.amount} to {self.phone_number} ({self.get_provider_display()})"


