
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello, world!")


def home(request):
    return HttpResponse("This is home page!")

def about(request):
    return HttpResponse("This is about page!")

