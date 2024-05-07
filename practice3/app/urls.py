from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name='index'),  # Assuming 'view' is the name of your view function
]
