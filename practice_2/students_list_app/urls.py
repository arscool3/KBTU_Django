from django.contrib import admin
from django.urls import path

from students_list_app.views import showList

urlpatterns = [
    path('', showList, name="student_list"),
]
