from rest_framework import serializers
from .models import Transaction
from .models import PaymentTransaction
from transactions.models import MoneyTransfer


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'created_at']

class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = ['id', 'category', 'amount', 'created_at']


class MoneyTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyTransfer
        fields = ['id', 'receiver_account_number', 'bank', 'amount', 'created_at']
