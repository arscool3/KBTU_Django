# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            return HttpResponse("Form submitted successfully!")
    else:
        form = MyForm()
    return render(request, 'index.html', {'form': form})
