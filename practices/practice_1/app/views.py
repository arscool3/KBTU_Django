from django.shortcuts import render

def home(request):
    message = "This is main view"
    return render(request, 'home.html', {'message': message})

def basic(request):
    message = "This is basic view"
    return render(request, 'base.html', {'message': message})

def test(request):
    message = "This is test view"
    return render(request, 'test.html', {'message': message})