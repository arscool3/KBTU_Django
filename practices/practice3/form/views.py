from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')
