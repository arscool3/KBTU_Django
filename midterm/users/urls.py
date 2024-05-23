from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),  
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  
]
