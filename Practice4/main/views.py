from django.shortcuts import render, HttpResponse, redirect
from .models import Client, Manager, Request
from .forms import UserCreationForm, RequestForm
from django.contrib.auth import authenticate, login, logout, forms
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            client = Client.objects.create(user_id=user.id, name=form.cleaned_data['first_name'], surname=form.cleaned_data['last_name'], email=form.cleaned_data['email'])
            client.save()
            return redirect('login')
    return render(request, 'log_reg.html', {'form': UserCreationForm})

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if user.is_staff:
                    return redirect('manager_page')
                else:
                    return redirect('application_page')
            except Exception:
                pass
        else:
            return render(request, 'log_reg.html', {'form': forms.AuthenticationForm(), 'comment': 'Wrong credentials, or you still do not have access to enter the Web page'})
    elif request.method == "GET":
        return render(request, 'log_reg.html', {'form': forms.AuthenticationForm()})

def application_page_view(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            client_user_id = request.user.id
            try:
                client = Client.objects.get(user_id=client_user_id)
            except:
                return render(request, 'log_reg.html', {'form': forms.AuthenticationForm(), 'comment': 'Wrong credentials, or you still do not have access to enter the Web page'})

            staff = User.objects.filter(is_staff=True, is_active=True).all().order_by('?').first()
            try:
                manager = Manager.objects.get(user_id=staff.id)
            except:
                return render(request, 'log_reg.html', {'form': forms.AuthenticationForm(), 'comment': 'Wrong credentials, or you still do not have access to enter the Web page'})

            client_request = Request(client=client, manager=manager, title=title, description=description)
            client_request.save()

    form = RequestForm()
    return render(request, 'application_page.html', {'form': form})

def manager_page_view(request):
    manager_user_id = request.user.id
    try:
        manager = Manager.objects.get(user_id=manager_user_id)
    except:
        return render(request, 'log_reg.html', {'form': forms.AuthenticationForm(), 'comment': 'Wrong credentials, or you still do not have access to enter the Web page'})

    requests = Request.objects.filter(manager=manager).exclude(status='completed')
    requests.update(status='in_progress')
    return render(request, 'manager_page.html', {'manager': manager, 'requests': requests})

def close_request_view(request, request_id):
    if request.method == 'POST':
        try:
            request_obj = Request.objects.get(id=request_id)
            request_obj.status = 'completed'
            request_obj.save()
            return redirect('manager_page')
        except:
            return redirect('manager_page')
