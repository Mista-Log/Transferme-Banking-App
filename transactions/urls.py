from django.urls import path
from .views import TransactionListView
from .views import PaymentTransactionListView
from transactions.views import MoneyTransferCreateView

urlpatterns = [
    path('initial-transaction/', TransactionListView.as_view(), name="transaction-list"),
    path('payments/', PaymentTransactionListView.as_view(), name="payment-list"),
    path('transfer/', MoneyTransferCreateView.as_view(), name="money-transfer"),
]