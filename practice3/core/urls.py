from django.urls import path

from core.views import add_student, add_event, add_organizer

urlpatterns = [
    path('event/', add_event, name='add_event'),
    path('student/', add_student, name='add_student'),
    path('organizer/', add_organizer, name='add_organizer'),
]