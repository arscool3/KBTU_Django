from django.urls import path
from . import views

urlpatterns = [
    path('tests/', views.test_list),
    path('tests/<int:pk>/', views.test_detail),
]
