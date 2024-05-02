from django.urls import path
from .views import *

urlpatterns = [
    path('university/', get_universities),
    path('faculties/', get_faculties),
    path('specialities/', get_specialities),
    path('students/', get_students),
]
