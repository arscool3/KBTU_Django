from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms


# Create your views here.
def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)


def logout_view(request):
    logout(request)
    return HttpResponse("You have logout")


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return HttpResponse("everything is ok")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': forms.AuthenticationForm()})


@decorators.login_required(login_url='login')
def check_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"{request.user} is authenticated")
    raise Exception(f"{request.user} is not authenticated")
