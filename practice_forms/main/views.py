from django.shortcuts import render
from django.http import HttpResponse

from main.forms import ComputerForm
from  main.models import Computer
# Create your views here.

def add_model(request, given_form):
    if request.method == 'POST':
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, computer was created')
    return render(request, 'index.html', {'form': given_form})

def addComputer(request):
    return add_model(request, ComputerForm)

def getComputers(request):
    compData = Computer.objects.all()
    return render(request, 'computers.html',{'computers': compData})