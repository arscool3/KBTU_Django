from django.shortcuts import render , redirect
from .forms import NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return redirect('thanks')
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')