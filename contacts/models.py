from django.db import models
from django.conf import settings

class Contact(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    favorite = models.BooleanField(default=False)
    avatar_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.account_number})"
