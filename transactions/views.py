from rest_framework import generics, permissions
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import generics, permissions
from .models import PaymentTransaction
from .serializers import PaymentTransactionSerializer
from transactions.models import MoneyTransfer
from transactions.serializers import MoneyTransferSerializer
from transactions.models import SIMTopUp
from transactions.serializers import SIMTopUpSerializer



class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)



class PaymentTransactionListView(generics.ListCreateAPIView):
    serializer_class = PaymentTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PaymentTransaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MoneyTransferCreateView(generics.CreateAPIView):
    serializer_class = MoneyTransferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class SIMTopUpCreateView(generics.CreateAPIView):
    serializer_class = SIMTopUpSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
