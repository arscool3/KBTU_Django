from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from website.views import NovelViewSet, UserProfileViewSet, ChapterViewSet, ReviewViewSet, BookmarkViewSet

router = DefaultRouter()
router.register(r'novels', NovelViewSet)
router.register(r'users', UserProfileViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'bookmarks', BookmarkViewSet)

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
