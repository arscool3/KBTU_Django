import dramatiq
from django.core.mail import send_mail
from django.contrib.auth.models import User
from journey_journal_back.settings import EMAIL_HOST_USER

@dramatiq.actor
def send_registration_email(user_id):
    user = User.objects.get(pk=user_id)
    subject = 'Registration Successful'
    message = f'Dear {user.username},\n\nThank you for registering on our website!'
    recipient_list = [user.email]
    send_mail(subject, message, EMAIL_HOST_USER, recipient_list)