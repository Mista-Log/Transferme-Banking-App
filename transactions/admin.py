from django.contrib import admin
from .models import Transaction
from .models import PaymentTransaction


admin.site.register(Transaction)
admin.site.register(PaymentTransaction)