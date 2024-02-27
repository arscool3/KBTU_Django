from django.shortcuts import redirect, render

# Create your views here.



from django.shortcuts import render, redirect, HttpResponse
from test_app.forms import NewCustomerForm


def main_view(request):
    form = NewCustomerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/test/basic')
    else:
        form = NewCustomerForm()
    context = {
        'form': form,
    }
    return render(request, 'basic.html', context)

def basic_view(request):
    return HttpResponse("This is basic view")

def test_view(request):
    return HttpResponse("This is test view")
