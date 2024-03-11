from django.urls import path
from blogApp.views import postView
urlpatterns = [path('', postView.get),]