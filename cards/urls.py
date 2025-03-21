from django.urls import path
from .views import CardListCreateView, CardDeleteView

urlpatterns = [
    path('', CardListCreateView.as_view(), name="card-list"),
    path('<int:pk>/delete/', CardDeleteView.as_view(), name="card-delete"),
]
