# website/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, NovelViewSet, ChapterViewSet, ReviewViewSet, BookmarkViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'novels', NovelViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'bookmarks', BookmarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
