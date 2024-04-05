from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, CheckAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('check/', CheckAPIView.as_view(), name='check'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]