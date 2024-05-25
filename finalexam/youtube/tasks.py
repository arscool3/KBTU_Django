from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task(subject, message, recipient_list):
    try:
        send_mail(subject, message, 'elshan.arsen.q@gmail.com', recipient_list)
        return "Successfully sent email"
    except Exception as e:
        return str(e)
