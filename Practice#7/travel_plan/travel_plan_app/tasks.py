# tasks.py
import dramatiq
from django.core.mail import send_mail
from .models import Trip

@dramatiq.actor
def send_trip_notification_email(trip_id):
    try:
        trip = Trip.objects.get(id=trip_id)
        subject = f"New Trip Created: {trip.destination}"
        message = f"Dear {trip.user.username},\n\nA new trip to {trip.destination} has been created. Enjoy your journey!"
        send_mail(subject, message, 'your@email.com', [trip.user.email])
    except Trip.DoesNotExist:
        pass
