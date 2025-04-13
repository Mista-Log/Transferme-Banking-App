from rest_framework import generics, permissions
from .models import Card
from .serializers import CardSerializer
from rest_framework import generics, permissions
from .models import Card
from .serializers import CardSerializer


class CardListCreateView(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CardDeleteView(generics.DestroyAPIView):
    queryset = Card.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

class CardCreateView(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]
