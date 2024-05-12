from celery import shared_task
from django.core.mail import send_mail
from .models import Employee, Task

@shared_task
def update_task_status(task_id, status):
    task = Task.objects.get(id=task_id)
    task.status = status
    task.save()

@shared_task
def notify_employee(employee_id, message):
    employee = Employee.objects.get(id=employee_id)
    send_mail(
        'Notification',
        message,
        'from@example.com',
        [employee.email],
        fail_silently=False,
    )
