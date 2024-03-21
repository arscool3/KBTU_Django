from django.urls import path

from myapp.views import get_teacher_by_name

urlpatterns = [
    path("teachers/", get_teacher_by_name, name='main'),
  
]