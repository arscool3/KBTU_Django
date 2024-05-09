from __future__ import absolute_import
from celery import Celery
from django.core.mail import send_mail
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_django.settings')

app = Celery("celery_django", broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task
def send_email(to, subject, message):
    try:
        send_mail(subject, message, 'a_madiyarbek@kbtu.kz', [to])
        print(f"Email sent successfully to {to}")
    except Exception as e:
        print(f"Failed to send email to {to}. Error: {e}")