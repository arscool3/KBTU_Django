from django.urls import path

from hello.views import index, other

urlpatterns = [
    path("", index, name='index'),
    path("today", other, name='other'),
]