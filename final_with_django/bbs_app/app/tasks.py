import dramatiq
from django.core.mail import send_mail
from django.conf import settings

@dramatiq.actor
def send_booking_confirmation(email, booking_id):
    send_mail(
        'Booking Confirmation',
        f'Your booking with ID {booking_id} has been confirmed.',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
