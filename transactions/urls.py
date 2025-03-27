from django.urls import path
from .views import TransactionListView
from .views import PaymentTransactionListView

urlpatterns = [
    path('initial-transaction/', TransactionListView.as_view(), name="transaction-list"),
    path('payments/', PaymentTransactionListView.as_view(), name="payment-list"),
]