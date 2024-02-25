from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse


# Function-based view
def hello_world(request):
    return HttpResponse("Function-based view")


# Class-based view using View
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Class-based view using View")


# Class-based view using TemplateView to render a template
class HomePageView(TemplateView):
    template_name = 'home.html'