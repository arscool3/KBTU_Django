from django.urls import path
from .views import add_student

urlpatterns = [
    path('add-student/', add_student, name='add_student'),
    # Add other paths as needed
]
