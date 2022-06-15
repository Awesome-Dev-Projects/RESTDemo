from django.urls import path
from .views import home_view, HomeAPIView


urlpatterns = [
    # path('',home_view,name='home'),
    path('', HomeAPIView.as_view(), name='home'),
]
