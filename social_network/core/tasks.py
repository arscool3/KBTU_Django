from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_task(subject, message, recipient_list):
    try:
        send_mail(subject, message, 'nursturugeldiev@gmail.com', recipient_list)
        return "Succesfully sent email"
    except Exception as e:
        print(e)
        return "Error sending email"