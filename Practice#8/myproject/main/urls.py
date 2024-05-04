from django.urls import path
from .views import TestView

urlpatterns = [
    path('tests/', TestView.as_view()),
    path('tests/<int:pk>/', TestView.as_view()),
]