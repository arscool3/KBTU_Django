
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'mainpage'),
    path('about', views.about, name = 'aboutpage')
]