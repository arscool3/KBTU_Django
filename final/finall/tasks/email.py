from celery import Celery
from fastapi import BackgroundTasks
from . import celery_app

@celery_app.task
def send_email_notification(email: str, message: str):
    # Logic to send email notification
    pass