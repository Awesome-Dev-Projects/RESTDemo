from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterUserView, CustomTokenObtainPairView

# JWT Token Authentication URLs
# urlpatterns = [
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='token_obtain_pair'),
    path('token/obtain/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
