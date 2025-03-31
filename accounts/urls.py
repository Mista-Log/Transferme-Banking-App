from django.urls import path
from .views import WalletDetailView
from accounts.views import BankListView

urlpatterns = [
    path('wallet/', WalletDetailView.as_view(), name="wallet-detail"),
    path('banks/', BankListView.as_view(), name="bank-list"),
]

