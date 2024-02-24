from django.shortcuts import render, redirect
import dataclasses
from django.http import HttpResponse
from .forms import TaskForm  # Import your TaskForm
from django.core.cache import cache

@dataclasses.dataclass
class Task:
    description: str
    checked: bool

def get_tasks():
    tasks = cache.get('tasks')
    if tasks is None:
        tasks = [
            Task('Clean room', False),
            Task('Do Homework', True),
            Task('Buy groceries', False),
        ]
        cache.set('tasks', tasks)
    return tasks

def view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_description = form.cleaned_data['task_inp']
            task = Task(description=task_description, checked=False)  # Create a new Task instance
            tasks = get_tasks()
            tasks.append(task)
            cache.set('tasks', tasks)
            return redirect('http://127.0.0.1:8000/myapp')  # Redirect after submission
    else:
        form = TaskForm()

    tasks = get_tasks()  # Fetch all tasks from the cache
    return render(request, 'index.html', {'form': form, 'tasks': tasks})
