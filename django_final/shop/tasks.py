import dramatiq
from django.core.mail import send_mail
from django.contrib.auth.models import User
#from django.template.loader import render_to_string
from django_final.settings import EMAIL_HOST_USER

@dramatiq.actor
def send_email(user_id):
    user = User.objects.get(pk=user_id)
    subject = 'Added order successfully'
    message = f'Dear {user.username},Thank you for your purchase!'
    recipient_list = [user.email]
    send_mail(subject, message, EMAIL_HOST_USER, recipient_list)

