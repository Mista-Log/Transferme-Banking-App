from django.urls import path
from .views import TransactionListView

urlpatterns = [
    path('initial-transaction/', TransactionListView.as_view(), name="transaction-list"),
]
