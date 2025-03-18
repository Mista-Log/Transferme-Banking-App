from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CARD_TYPES = (
    ("visa", "Visa"),
    ("mastercard", "MasterCard"),
    ("amex", "American Express"),
)

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")
    card_type = models.CharField(max_length=20, choices=CARD_TYPES)
    last4 = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.card_type} ****{self.last4}"
