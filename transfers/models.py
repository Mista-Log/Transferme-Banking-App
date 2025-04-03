# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TransferRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
        ("canceled", "Canceled"),
    ]

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_requests")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_requests")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} → {self.receiver.username} (${self.amount}) - {self.status}"
