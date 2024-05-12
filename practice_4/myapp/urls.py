from django.urls import path
from . import views

urlpatterns = [
    path('model1/', views.list_model1, name='list_model1'),
    path('model1/create/', views.create_model1, name='create_model1'),
    # Add more paths for other views
]
