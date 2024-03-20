from django.shortcuts import render

students = ['arslan', 'yernur']

def view(request):
    return render(request, 'index.html', {'students': students})