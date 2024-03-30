from django.urls import path
from rest_framework import routers
from main.views import index, login_view, logout_view, users, authors, books, categories, consumers, reviews, get_book
from main.views2 import CategoryViewSet

router = routers.SimpleRouter()

router.register(r'category', CategoryViewSet)

urlpatterns = [
  path('', index, name='index'),
  path('login/', login_view, name='login'),
  path("logout/", logout_view, name='logout'),
  
  # Get methods
  path('users/', users, name='users'),
  path('authors/', authors, name='authors'),
  # path('categories/', categories, name='categories'),
  path('books/', books, name='books'),
  path('books/<int:id>', get_book, name='get_book'),
  path('consumers/', consumers, name='consumers'),
  path('reviews/', reviews, name='reviews'),
] + router.urls