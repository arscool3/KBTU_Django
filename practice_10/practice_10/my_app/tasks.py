# tasks.py
from django.core.mail import send_mail
from dramatiq import actor

@actor
def send_email_task(subject, message, recipient_list):
    """
    Task to send an email.
    """
    send_mail(subject, message, 'your_email@example.com', recipient_list)