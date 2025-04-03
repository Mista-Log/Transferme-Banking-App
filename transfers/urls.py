from django.urls import path
from .views import TransferRequestView, UpdateTransferRequestView, CancelTransferRequestView

urlpatterns = [
    path('requests/', TransferRequestView.as_view(), name="transfer-request-list"),  # List & Create
    path('requests/<int:pk>/update/', UpdateTransferRequestView.as_view(), name="transfer-request-update"),  # Accept/Decline
    path('requests/<int:pk>/cancel/', CancelTransferRequestView.as_view(), name="transfer-request-cancel"),  # Cancel
]
