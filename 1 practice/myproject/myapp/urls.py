from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('basic/', views.basic_view, name='basic'),
    path('test/', views.test_view, name='test'),
]
