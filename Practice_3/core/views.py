from django.shortcuts import render
from .forms import UserForm
from .models import User

def user_create_view(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form, 'users': users})