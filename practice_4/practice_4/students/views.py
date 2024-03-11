from django.shortcuts import render
from .forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            # For example, save to the database
            form.save()
            # Redirect or render success page
    else:
        form = MyForm()
    
    return render(request, 'my_template.html', {'form': form})
