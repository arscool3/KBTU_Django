from django.urls import path
from helloworld.views import index,exp

urlpatterns = [
    path('',index,name="index"),
    path('exp/<int:id>',exp,name="exp")
]