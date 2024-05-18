from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authorization.urls')),  # добавьте эту строку
    path('', include('app.urls')),
]
