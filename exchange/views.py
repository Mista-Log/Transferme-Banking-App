from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer

class ExchangeRateListView(generics.ListAPIView):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    permission_classes = [permissions.AllowAny]
