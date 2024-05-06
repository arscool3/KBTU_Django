from django.urls import path
from main import views

urlpatterns = [
    # Add the URL pattern for the root URL of your app
    path('', views.index, name='index'),
]
