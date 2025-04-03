from rest_framework import serializers
from .models import TransferRequest

class TransferRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferRequest
        fields = '__all__'
        read_only_fields = ['sender', 'status']
