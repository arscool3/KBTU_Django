from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import CustomLoginView, RefreshTokenView, RegisterView, UserViewSet, LinkViewSet, ClickViewSet, CategoryViewSet, TagViewSet, LinkUsageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'links', LinkViewSet)
router.register(r'clicks', ClickViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'linkusages', LinkUsageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
]
