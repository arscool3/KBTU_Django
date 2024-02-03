from django.urls import path

from hello.views import *

urlpatterns = [
    path("", index, name='index'),
    path("basic", basic, name='basic'),
    path("test", test, name='test'),
]