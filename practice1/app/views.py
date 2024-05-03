from django.http import HttpResponse

import random

# Create your views here.
car_replies = [
    "meow",
    "prr",
    "hiss",
    "*cat just ignores you :(*"
]


def index(request):
    return HttpResponse("Hello World!")


def cat(request):
    return HttpResponse(random.choice(car_replies))


def divide(request, number):
    return HttpResponse(number / 2)