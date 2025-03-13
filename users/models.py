from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    is_verified = models.BooleanField(default=False)  # Email verification status

    REQUIRED_FIELDS = ['email']  # Email is required for signup

    def __str__(self):
        return self.username
