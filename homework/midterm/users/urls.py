
from django.urls import path,include
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
	path('register',Register.as_view(),name="register")
]
