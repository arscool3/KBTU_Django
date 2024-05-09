from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", UserRegistrationAPIView.as_view(), name="registration"),
    path("signin/", UserLoginAPIView.as_view(), name="login"),
]