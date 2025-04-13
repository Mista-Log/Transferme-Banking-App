from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

User = get_user_model()

CARD_TYPES = (
    ("visa", "Visa"),
    ("mastercard", "MasterCard"),
    ("amex", "American Express"),
)



class Card(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20, unique=True)
    holder_name = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=5)  # Format MM/YY
    cvv = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    color = models.CharField(max_length=20, default="#000000")  # Hex or class

    def __str__(self):
        return f"{self.holder_name} - {self.card_number}"