from django.contrib import admin
from django.urls import path
from studentsapp.views import view_students  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', view_students),  # Add this line
]
