from django.db import models

# Create your models here.


class ExchangeRate(models.Model):
    base_currency = models.CharField(max_length=10)
    target_currency = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.base_currency} to {self.target_currency} - {self.rate}"
