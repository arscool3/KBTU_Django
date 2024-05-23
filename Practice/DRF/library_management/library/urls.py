from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, PublisherViewSet, CategoryViewSet, BookViewSet, MemberViewSet, BorrowViewSet
from . import views

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrows', BorrowViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls)),  
]
