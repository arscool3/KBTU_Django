from django.urls import path

from practice2.views import *

urlpatterns = [
    # Practice - 2
    path("", index, name='index'),
]