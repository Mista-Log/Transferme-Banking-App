from django.urls import path
from .views import ATMListView

urlpatterns = [
    path('list/', ATMListView.as_view(), name="atm-list"),
]
