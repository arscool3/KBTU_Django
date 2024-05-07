from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login , name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.registration, name='register'),
    path('home/', views.homepage, name='home'),
]
