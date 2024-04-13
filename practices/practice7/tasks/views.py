from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from dramatiq import actor
from django.core.mail import send_mail

@actor
def send_task_notification(task_title):
    send_mail(
        'New Task Created',
        f'A new task "{task_title}" has been created.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            send_task_notification.send(task.title)
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
