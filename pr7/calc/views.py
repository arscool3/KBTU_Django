from django.shortcuts import render

from .tasks import add


def index(request):
    if request.method == 'POST':
        add.send(float(request.POST["a"]), float(request.POST["b"]))
    return render(request, "index.html")
