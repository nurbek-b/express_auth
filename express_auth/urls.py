from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import registration


urlpatterns = [
    path('jwtauth/register/', registration, name='register'),
    path("jwtauth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("jwtauth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]