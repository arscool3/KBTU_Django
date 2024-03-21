from django.shortcuts import render
from django.http import HttpResponse
from .forms import BasicForm


def my_view(request):
    return HttpResponse("Dias is retaker!")


def contact_view(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'success.html')
    else:
        form = BasicForm()
    return render(request, 'hello.html', {'form': form})
