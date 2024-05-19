from celery import shared_task
from .models import Task


@shared_task
def update_task_status(task_id, status):
    try:
        task = Task.objects.get(id=task_id)
        task.status = status
        task.save()
    except Task.DoesNotExist:
        pass
