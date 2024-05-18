from __future__ import absolute_import
from celery import Celery,shared_task
import os
import requests
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final.settings')

app = Celery("final")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

logger = logging.getLogger(__name__)

@shared_task
def send_notification(user_id, content):
    url = 'http://127.0.0.1:8000/api/v1/notifications/'
    payload = {
        'user': user_id,
        'content': content
    }
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status() 
        logger.info("Notification created successfully.")
    except requests.RequestException as e:
        logger.error(f"Failed to create notification: {e}")