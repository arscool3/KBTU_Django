from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Assuming you have a model named User with name and email fields
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            User.objects.create(name=name, email=email)  # Save the data to the database
            return redirect('success_url')

    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})


def success(request):
    return render(request, 'success.html')