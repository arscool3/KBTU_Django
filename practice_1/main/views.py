from django.shortcuts import render
from django.http import HttpResponse
from django import template

todo_list = {
    'Finish assignment': 1,
    'Sport': 2,
    'Read a book': 2,
    'Play tennis': 3,
}
    
def index(request):
    return render(request, "index.html", {
        'todo_list': todo_list
    })

