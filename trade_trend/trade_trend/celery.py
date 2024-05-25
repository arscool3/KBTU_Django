from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trade_trend.settings')

app = Celery('trade_trend')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
