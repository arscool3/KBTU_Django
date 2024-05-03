import dramatiq
from django.core.mail import send_mail
from my_app.models import Book

@dramatiq.actor
def send_notification_email(book_id):
    try:
        book = Book.objects.get(pk=book_id)
        # You can customize the email content as per your requirements
        subject = f"New Book Added: {book.title}"
        message = f"A new book '{book.title}' has been added to our collection."
        recipient_list = list(book.authors.values_list('email', flat=True))  # Assuming authors have emails
        sender_email = 'your_email@example.com'  # Change this to your email
        send_mail(subject, message, sender_email, recipient_list)
    except Book.DoesNotExist:
        # Handle the case when the book with the given ID does not exist
        pass
