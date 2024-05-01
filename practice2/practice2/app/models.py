from django.db import models

# Create your models here.
urlpatterns = [
    path('books/', book_list_view, name='student_list'),
]