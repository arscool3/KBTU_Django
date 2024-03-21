from django.shortcuts import render
from django.http import HttpResponse


todo_list = [
    "brush teeth",
    "do homework",
    "go sleep"
]

def index(request):
    return render(request, "index.html", {
        'todo_list': todo_list
    })

def test(request, id):
    return HttpResponse(f"5 times id = {5 * id}")