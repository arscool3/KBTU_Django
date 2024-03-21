from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('practice_week3_task/', include('practice_week3_task.urls')),
]