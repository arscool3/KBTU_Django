from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('Library.urls')),
    path('authentication/', include('Authentication.urls'))
]
