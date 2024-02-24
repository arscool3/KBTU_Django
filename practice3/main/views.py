from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person

def form_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            form = PersonForm()
            allPeople = Person.objects.all()
            return render(request, 'form_template.html', {'form': form, 'allPeople': allPeople})
    else:
        form = PersonForm()
    allPeople = Person.objects.all()
    return render(request, 'form_template.html', {'form': form, 'allPeople': allPeople})


