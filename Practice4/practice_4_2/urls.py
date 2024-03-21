
from django.urls import path
from practice_4.views import get_authors, get_publishers

urlpatterns = [
    path('authors/', get_authors, name='get_authors'),
    path('publishers/', get_publishers, name='get_publishers'),
]