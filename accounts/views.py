from django.shortcuts import render
from rest_framework import generics, permissions
from accounts.models import Bank
from accounts.serializers import BankSerializer

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Wallet
from .serializers import WalletSerializer

class WalletDetailView(generics.RetrieveAPIView):
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.wallet


class BankListView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.AllowAny]
