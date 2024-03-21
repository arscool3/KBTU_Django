from django.contrib import admin
from django.urls import path, include   # Include the 'include' module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]


