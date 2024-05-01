from django.shortcuts import render

# Create your views here.

students = ['arslan', 'yernur']

def view(request):
    return render(request, 'index.html', {'students': students})