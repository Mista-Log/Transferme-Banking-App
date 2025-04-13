
from django.db import models

class ATM(models.Model):
    name = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    distance_km = models.FloatField(null=True, blank=True)  # Optionally calculated dynamically

    def __str__(self):
        return f"{self.bank} - {self.address}"
