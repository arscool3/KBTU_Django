from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users import views

urlpatterns = [
    path(r'users/', views.UserViewSet.as_view({'post': 'create_user'})),
    path(r'users/user/', views.UserViewSet.as_view({'get': 'get_user'})),
    path(r'users/update/', views.UserViewSet.as_view({'put': 'update_user'})),
    path(r'users/verify/', views.UserViewSet.as_view({'post': 'verify_user'})),
    path(r'users/token/', views.UserViewSet.as_view({'post': 'create_token'})),
    path(r'users/token/refresh/', TokenRefreshView.as_view()),
]
