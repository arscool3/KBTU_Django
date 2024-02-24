from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    return HttpResponse("Welcome to our website!")

def about(request):

    return render(request, 'about.html')

def contact(request):

    if request.method == 'POST':
        pass
    return render(request, 'contact.html')
