from django.urls import path

from hello.views import *

urlpatterns = [
    # Practice - 1
    path("", index, name='index'),
    path("basic", basic, name='basic'),
    path("test", test, name='test'),

]