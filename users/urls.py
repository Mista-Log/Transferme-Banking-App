from django.urls import path, include
from .views import UserSignupView, UserProfileUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import DashboardAPIView

urlpatterns = [
    # Custom Signup API
    path('register/', UserSignupView.as_view(), name='user-register'),
    
    # JWT Authentication
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # User Profile Update API
    path('profile/', UserProfileUpdateView.as_view(), name='user-profile'),
    
    # dj-rest-auth (Login, Logout, Password Reset)
    path('auth/', include('dj_rest_auth.urls')),

    # dj-rest-auth Registration (Optional, includes signup)
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    # AllAuth Social Authentication (Google & Facebook)
    path('auth/social/', include('allauth.socialaccount.urls')),

    path("dashboard/", DashboardAPIView.as_view(), name="user-dashboard"),
]


