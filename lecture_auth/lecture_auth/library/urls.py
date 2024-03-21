from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from library.views import UserCreateView, UserUpdateView, UserRetrieveView

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('signup/', UserCreateView.as_view()),
    path('password/<int:pk>/', UserUpdateView.as_view()),
    path('userinfo/', UserRetrieveView.as_view())
]