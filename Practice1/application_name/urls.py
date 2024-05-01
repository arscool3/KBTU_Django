from django.urls import path

from .views import main, basic, test_view

urlpatterns = [
    path("main", main, name='main'),
    path("basic", basic, name='basic'),
    path("test_view", test_view, name='test_view'),
]