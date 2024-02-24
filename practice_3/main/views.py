from django.shortcuts import render, redirect
from .forms import BookForm

def create_book(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      instance = form.save()
      return redirect('success.html')
  else:
    form = BookForm()

  return render(request, 'index.html', {'form': form})