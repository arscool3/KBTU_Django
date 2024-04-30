import dramatiq
from django.core.mail import send_mail
from django.conf import settings
from .models import Book

@dramatiq.actor
def notify_user_on_new_book(book_id):
    book = Book.objects.get(id=book_id)
    user_email = "madina@example.com" 
    subject = "New Book Alert"
    message = f"A new book '{book.title}' by {book.author.name} has been added."
    from_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, from_email, [user_email])
