from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from final.authorization.views import UserViewSet

router = DefaultRouter()
router.register(r'auth', UserViewSet, basename='auth')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('auth/', include('authorization.urls')),
    path('', include(router.urls))
]

