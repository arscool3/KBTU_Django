from django.shortcuts import render, redirect
from .models import Task, User
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})
