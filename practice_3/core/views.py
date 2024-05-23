from django.shortcuts import render
from django.http import HttpResponse

from core.forms import ProductForm
from core.models import Product

# Create your views here.
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, product was created')
    
    return render(request, 'index.html', {'form': ProductForm()})
