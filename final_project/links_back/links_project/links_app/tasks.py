# tasks.py
from celery import shared_task
from .models import Link, LinkUsage

@shared_task
def update_link_usage(link_id):
    link = Link.objects.get(id=link_id)
    usage = LinkUsage.objects.get(link=link)
    usage.clicks = link.clicks.count()
    usage.save()
