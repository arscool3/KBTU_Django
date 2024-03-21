from django.urls import path
from .views import *
urlpatterns = [
    path('hello/<str:name>', sayHello, name='hello'),
    path('time/', getTime, name='time'),
    path('view1/', view1),
    path('view2/', view2),
    path('view3/', view3)
]