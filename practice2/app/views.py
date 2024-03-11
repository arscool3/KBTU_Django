from django.shortcuts import render

# Create your views here.
students = [
    'Nurgalym', 'Aslanbek', 'Altair'
]

def view(request):
    return render(request, 'index.html', {'students': students})