from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name= "main"),
    path('basic/', views.basic_view, name = "basic"),
    path('test/', views.test_view, name='test'),
]