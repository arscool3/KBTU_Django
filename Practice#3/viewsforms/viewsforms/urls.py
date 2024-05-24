"""viewsforms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    # urls.py
from django.urls import path
from myapp.views import my_view

urlpatterns = [
    path('my-form/', my_view, name='my_form'),
    # Add other URLs as needed
]

"""
from django.contrib import admin
from django.urls import path
from main.views import my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-form/' , my_view , name='my_form')
]
