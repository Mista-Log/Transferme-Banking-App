from django.urls import path, include
from .views import UserSignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserSignupView.as_view(), name='user-register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('dj_rest_auth.urls')),  # Login, Logout, Password Reset
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Signup
    path('auth/google/', include('allauth.socialaccount.urls')),  # Google Auth
    path('auth/facebook/', include('allauth.socialaccount.urls')),  # Facebook Auth
]

