from django.shortcuts import render , redirect
from .forms import NewForm

def get_name(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            return redirect('thanks')
    else:
        form = NewForm()
    return render(request, 'name.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')