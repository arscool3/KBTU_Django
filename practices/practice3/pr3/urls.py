from django.urls import path
from . import views

urlpatterns = [
    path("test/",views.test,name="test"),
    path("",views.people,name="people"),
    path("dudes/<str:fn>",views.dudes,name="dudes")
]