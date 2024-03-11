from django.shortcuts import render, redirect
from .forms import MyForm
# Create your views here.
from django.http import HttpResponse
from .models import MyModel

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            MyModel.objects.create(name=name, email=email)
            return redirect('success') 
    else:
        form = MyForm()
    return render(request, 'template.html', {'form': form})

def success_auth(request):
    return render(request, 'success.html')