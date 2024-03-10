from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .serializers import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

class CustomUserCreationView(CreateView):
    template_name = 'registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
