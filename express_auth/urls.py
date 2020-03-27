from django.urls import path, re_path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import registration, activate


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    # path('auth/', include('rest_framework.urls')),
    path('register/', registration, name='register'),
    path("jwtauth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("jwtauth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate, name='activate'),
    
]