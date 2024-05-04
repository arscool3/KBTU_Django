from __future__ import absolute_import
from celery import Celery
from django.core.mail import send_mail
import os

# Установка модуля настроек Django для приложения 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_django.settings')

# Создание экземпляра Celery
app = Celery("celery_django")

# Получение настроек Django для Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузка tasks.py в приложение Django
app.autodiscover_tasks()

# Определение задачи отправки электронной почты
@app.task
def send_email(to, subject, message):
    try:
        # Отправка электронного письма с помощью функции send_mail Django
        send_mail(subject, message, 'your_email@example.com', [to])
        print(f"Email sent successfully to {to}")
    except Exception as e:
        print(f"Failed to send email to {to}. Error: {e}")
