from django.urls import path
from .views import WalletDetailView
from accounts.views import BankListView
from accounts.views import RequestOTPView, VerifyOTPView

urlpatterns = [
    path('wallet/', WalletDetailView.as_view(), name="wallet-detail"),
    path('banks/', BankListView.as_view(), name="bank-list"),
    path('otp/request/', RequestOTPView.as_view(), name="request-otp"),
    path('otp/verify/', VerifyOTPView.as_view(), name="verify-otp"),
]



