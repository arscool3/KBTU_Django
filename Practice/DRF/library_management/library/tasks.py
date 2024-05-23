import os
import django
import dramatiq
from .models import Book

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_management.settings')
django.setup()

@dramatiq.actor
def update_book_availability(book_id):
    book = Book.objects.get(id=book_id)
    book.save()
