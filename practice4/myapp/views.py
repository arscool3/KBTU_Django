from django.shortcuts import render, redirect
from .models import Model1, Model2, Model3, Model4
from .forms import Model1Form

def list_model1(request):
    items = Model1.objects.all()
    return render(request, 'myapp/model1_list.html', {'items': items})

def create_model1(request):
    if request.method == 'POST':
        form = Model1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_model1')
    else:
        form = Model1Form()
    return render(request, 'myapp/model1_form.html', {'form': form})