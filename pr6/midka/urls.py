from django.urls import path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'Person', PersonViewSet)


urlpatterns = [
    path('index', index, name='index'),
    path('add_book', add_book, name='add_book'),
    path('add_author', add_author, name='add_author'),
    path('add_publisher', add_publisher, name='add_publisher'),
    path('add_genre', add_genre, name='add_genre'),
    path('add_customer', add_customer, name='add_customer'),
    path('user/<int:user_id>/borrow', borrow_book, name='borrow_book'),
    path('user/<int:user_id>', get_user, name='get_user'),
] + router.urls

