from django.shortcuts import render, redirect
from .forms import ItemForm
# Create your views here.

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_created')
    else:
        form = ItemForm()
    return render(request, 'myapp/item_create.html', {'form': form})

def item_created(request):
    return render(request, 'myapp/item_created.html')