from rest_framework import serializers
from .models import Wallet
from accounts.models import Bank
from accounts.models import OTPVerification



class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance']

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name']
class OTPRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

class OTPVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp_code = serializers.CharField(max_length=5)
