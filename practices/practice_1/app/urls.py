from django.urls import path
from .views import home, basic, test

urlpatterns = [
    path('', home, name='home'),
    path('base/', basic, name='base'),
    path('test/', test, name='test'),
]
