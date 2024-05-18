from django.urls import path

from .views import add_user, add_courier, create_oder

urlpatterns = [
    path('user/', add_user, name='add_user'),
    path('courier/', add_courier, name='add_courier'),
    path('order/', create_oder, name='create_order'),
]