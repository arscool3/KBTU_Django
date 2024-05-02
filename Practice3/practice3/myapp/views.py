from django.shortcuts import render
from .forms import ItemForm


def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = ItemForm()
    return render(request, 'create_item.html', {'form': form})
