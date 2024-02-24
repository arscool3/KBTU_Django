from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Create a new MyModel object and save it
            new_entry = MyModel(name=name, time=time)
            new_entry.save()
            return render(request, 'heloo.html', {'name': name, 'time':time})
    
    form = MyForm()
    return render(request, 'my_template.html', {'form': form})       