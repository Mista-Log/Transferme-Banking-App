
from rest_framework import generics
from .models import ATM
from .serializers import ATMSerializer

class ATMListView(generics.ListAPIView):
    queryset = ATM.objects.all()
    serializer_class = ATMSerializer
