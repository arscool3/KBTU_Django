from django.urls import path
from app.views import get_students

urlpatterns = [
    path('', get_students, name='get_students')
]
