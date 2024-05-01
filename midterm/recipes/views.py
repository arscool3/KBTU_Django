from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CustomLoginView(LoginView):
  template_name = 'auth/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self) -> str:
    return reverse_lazy('recipes')
  
class CustomLogoutView(LogoutView):
  next_page = 'login'

def home(request):
  return render(request, 'home.html')

class RecipeList(ListView):
  model = Recipe
  context_object_name = 'recipes'
  
class RecipeDetail(DetailView):
  model = Recipe
  context_object_name = 'recipe'
  slug_field = 'id'
  slug_url_kwarg = 'id'

class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  fields = '__all__'
  success_url = reverse_lazy('recipes')

class RecipeUpdate(LoginRequiredMixin, UpdateView):
  model = Recipe
  fields = '__all__'
  success_url = reverse_lazy('recipes')
  slug_field = 'id'
  slug_url_kwarg = 'id'

class RecipeDelete(LoginRequiredMixin, DeleteView):
  model = Recipe
  context_object_name = 'recipe'
  success_url = reverse_lazy('recipes')
  slug_field = 'id'
  slug_url_kwarg = 'id'