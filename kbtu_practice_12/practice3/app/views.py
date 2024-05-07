from django.shortcuts import render
from .forms import MyForm
from .models import Person

def lesson4view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            form = MyForm()
            allPeople = Person.objects.all()
            return render(request, 'form.html', {'form': form, 'allPeople:': allPeople})
    else:
        form = MyForm()
    allPeople = Person.objects.all()
    return render(request, 'form.html', {'form': form, 'allPeople:': allPeople})