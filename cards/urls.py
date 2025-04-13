from django.urls import path
from .views import CardListCreateView, CardDeleteView
from .views import CardCreateView


urlpatterns = [
    path('', CardListCreateView.as_view(), name="card-list"),
    path('<int:pk>/delete/', CardDeleteView.as_view(), name="card-delete"),
    path('add/', CardCreateView.as_view(), name='add-card'),
]

