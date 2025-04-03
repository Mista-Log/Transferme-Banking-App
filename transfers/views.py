from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import TransferRequest
from .serializers import TransferRequestSerializer

# Create & View Transfer Requests
class TransferRequestView(generics.ListCreateAPIView):
    serializer_class = TransferRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Show requests where the user is the sender or receiver."""
        return TransferRequest.objects.filter(sender=self.request.user) | TransferRequest.objects.filter(receiver=self.request.user)

    def perform_create(self, serializer):
        """Automatically set sender to the logged-in user."""
        serializer.save(sender=self.request.user)

# Accept or Decline a Request
class UpdateTransferRequestView(generics.UpdateAPIView):
    serializer_class = TransferRequestSerializer
    permission_classes = [IsAuthenticated]
    queryset = TransferRequest.objects.all()

    def update(self, request, *args, **kwargs):
        """Only the receiver can accept or decline a request."""
        instance = self.get_object()
        
        if instance.receiver != request.user:
            return Response({"error": "You can only accept/decline requests sent to you."}, status=status.HTTP_403_FORBIDDEN)

        new_status = request.data.get("status")
        if new_status not in ["accepted", "declined"]:
            return Response({"error": "Invalid status."}, status=status.HTTP_400_BAD_REQUEST)

        instance.status = new_status
        instance.save()
        return Response(TransferRequestSerializer(instance).data)

# Cancel a Pending Request
class CancelTransferRequestView(generics.DestroyAPIView):
    serializer_class = TransferRequestSerializer
    permission_classes = [IsAuthenticated]
    queryset = TransferRequest.objects.all()

    def delete(self, request, *args, **kwargs):
        """Only the sender can cancel a pending request."""
        instance = self.get_object()

        if instance.sender != request.user:
            return Response({"error": "You can only cancel your own transfer requests."}, status=status.HTTP_403_FORBIDDEN)

        if instance.status != "pending":
            return Response({"error": "Only pending requests can be canceled."}, status=status.HTTP_400_BAD_REQUEST)

        instance.status = "canceled"
        instance.save()
        return Response({"message": "Transfer request canceled."}, status=status.HTTP_200_OK)
