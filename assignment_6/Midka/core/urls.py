from django.urls import path, include
from . import views
from rest_framework import routers
from .views import AuthorViewSet, GenreViewSet, BookViewSet
app_name = 'core'

router = routers.DefaultRouter()
router.register(r"authors", AuthorViewSet, basename='authors')
router.register(r"genres", GenreViewSet, basename='genres')
router.register(r"books", BookViewSet, basename='books')


urlpatterns = [
    path('', views.login_view, name='login'),
    path('', include(router.urls)),
    path('home/', views.home, name='home'),
    path('book-list', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
    path('register/', views.register_user, name='register'),
    path('create-book/', views.create_book, name='create-book'),
    path('logout/', views.logout_view, name='logout'),
]