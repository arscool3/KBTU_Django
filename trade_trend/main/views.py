from django.shortcuts import render


def get_index(request):
    return render(request, "index.html")


def get_user(request):
    return "Hello"