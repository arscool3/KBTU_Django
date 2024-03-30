from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Product, Category, Customer, Cart, CartItem, Order
from .forms import ProductForm, CategoryForm, CustomerForm, OrderForm
from django.views.generic import TemplateView
from django.views.generic import View
from django.contrib.auth import authenticate, login, decorators, logout, forms

from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from core.serializers import CustomerSerializer

#Authorization

# def basic_form(request, given_form):
#     if request.method == 'POST':
#         form = given_form(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("OK")
#         else:
#             raise Exception(f"some erros {form.errors}")
#     return render(request, 'authorization/index.html', {'form': given_form()})

# def logout_view(request):
#     logout(request)
#     return HttpResponse("You have logged out")


# def login_view(request):
#     if request.method == 'POST':
#         form = forms.AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             try:
#                 user = authenticate(**form.cleaned_data)
#                 login(request, user)
#                 if next := request.GET.get("next"):
#                     return redirect(next)
#                 return HttpResponse("everything is ok")
#             except Exception:
#                 return HttpResponse("something is not ok")
#         else:
#             raise Exception(f"some erros {form.errors}")
#     return render(request, 'authorization/index.html', {'form': forms.AuthenticationForm()})


# def register_view(request):
#     return basic_form(request, forms.UserCreationForm)

# #Home, About

# class HomeView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = Product.objects.all()
#         return context

# class AboutView(TemplateView):
#     template_name = 'about.html'



class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'id'

    @action(detail=True, methods=["get"])
    def get_by_id(self, request, id:int):
        customer = self.get_object()
        if customer.username == "Madi":
            return Response("You need an umbrella")
        return Response("You don't need an umbrella")



