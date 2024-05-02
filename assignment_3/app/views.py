from django.shortcuts import render, redirect
from .forms import userForm

def view(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = userForm()
    return render(request, 'index.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')