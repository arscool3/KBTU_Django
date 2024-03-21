from django.urls import path
from .views import hello_world, HelloWorldView, HomePageView

urlpatterns = [
    path('hello/', hello_world),
    path('hello-class/', HelloWorldView.as_view()),
    path('home/', HomePageView.as_view()),
]