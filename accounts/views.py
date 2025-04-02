from django.shortcuts import render
from rest_framework import generics, permissions
from accounts.models import Bank
from accounts.serializers import BankSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import OTPVerification
from accounts.serializers import OTPRequestSerializer, OTPVerifySerializer
from django.contrib.auth import get_user_model

User = get_user_model()



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

class RequestOTPView(APIView):
    """Generate and send OTP"""
    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            
            user, created = User.objects.get_or_create(username=phone_number, defaults={'phone_number': phone_number})
            otp_obj, _ = OTPVerification.objects.get_or_create(user=user, phone_number=phone_number)
            otp_code = otp_obj.generate_otp()
            
            # Simulate sending OTP via SMS (you can integrate Twilio or any SMS provider)
            print(f"📩 OTP Sent to {phone_number}: {otp_code}")  # Replace with real SMS logic
            
            return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPView(APIView):
    """Verify OTP"""
    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            otp_code = serializer.validated_data['otp_code']
            
            try:
                otp_obj = OTPVerification.objects.get(phone_number=phone_number, otp_code=otp_code)
                if otp_obj.is_valid():
                    otp_obj.delete()  # OTP should not be reused
                    return Response({"message": "Phone number verified successfully"}, status=status.HTTP_200_OK)
                return Response({"error": "OTP expired"}, status=status.HTTP_400_BAD_REQUEST)
            except OTPVerification.DoesNotExist:
                return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
