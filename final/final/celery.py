from __future__ import absolute_import
from celery import Celery
from django.core.mail import send_mail
import os
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_django.settings')

app = Celery("celery_django", broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task
def send_notification(user_id, content):
    url = 'http://localhost:8000/api/notifications/'
    payload = {
        'user': user_id,
        'content': content
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print("Notification created successfully.")
    else:
        print(f"Failed to create notification. Status code: {response.status_code}")