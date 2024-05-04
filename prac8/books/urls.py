# project/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # Other URL patterns
    path('api/', include(router.urls)),
]
