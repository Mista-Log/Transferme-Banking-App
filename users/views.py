from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSignupSerializer, UserLoginSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSignupSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from accounts.models import Account
from transactions.models import Transaction
from cards.models import Card
from notifications.models import Notification

User = get_user_model()


User = get_user_model()


class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "message": "User registered successfully",
            "user": UserSignupSerializer(user).data
        }, status=status.HTTP_201_CREATED)


# User Login View
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


# User Profile Update View
class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Get the authenticated user's profile

class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Fetch the user's account balance
        try:
            account = Account.objects.get(user=user)
            balance = account.balance
        except Account.DoesNotExist:
            balance = 0.0  # Default balance if no account exists

        # Fetch user's linked cards
        cards = Card.objects.filter(user=user)
        card_data = [
            {"card_type": card.card_type, "last4": card.last4, "balance": card.balance}
            for card in cards
        ]

        # Fetch recent transactions
        transactions = Transaction.objects.filter(user=user).order_by("-created_at")[:5]
        transaction_data = [
            {
                "amount": txn.amount,
                "transaction_type": txn.transaction_type,
                "date": txn.created_at.strftime("%d %B %Y"),
                "from": txn.sender.username if txn.sender else "N/A",
                "to": txn.receiver.username if txn.receiver else "N/A",
            }
            for txn in transactions
        ]

        # Fetch recent notifications
        notifications = Notification.objects.filter(user=user).order_by("-created_at")[:5]
        notification_data = [
            {"message": notif.message, "date": notif.created_at.strftime("%d %B %Y")}
            for notif in notifications
        ]

        return Response(
            {
                "current_balance": balance,
                "linked_cards": card_data,
                "recent_transactions": transaction_data,
                "recent_notifications": notification_data,
            }
        )
