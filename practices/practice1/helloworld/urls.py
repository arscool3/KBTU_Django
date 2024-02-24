from django.urls import path
from helloworld.views import index,exp,welcome

urlpatterns = [
    path('',index,name="index"),
    path('exp/<int:id>',exp,name="exp"),
    path('welcome/',welcome,name="welcome")
]