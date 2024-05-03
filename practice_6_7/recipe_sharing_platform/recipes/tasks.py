import dramatiq
from django.core.mail import send_mail
from .models import Registration

@dramatiq.actor
def send_registration_confirmation_email(user_id):
    user = User.objects.get(pk=user_id)
    registration = Registration.objects.get(user=user)

    subject = 'Registration Confirmation'
    message = f'Dear {user.username},\n\nThank you for registering on our website.'
    send_mail(subject, message, 'from@example.com', [user.email])
    registration.confirmation_email_sent = True
    registration.save()
