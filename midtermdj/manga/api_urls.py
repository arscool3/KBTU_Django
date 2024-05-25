from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, MangaViewSet, ChapterViewSet, PageViewSet, ReviewViewSet, UserProfileViewSet, UserViewSet

router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'mangas', MangaViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'pages', PageViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'userprofile', UserProfileViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
