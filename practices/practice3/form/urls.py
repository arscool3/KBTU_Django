from django.urls import path
from .views import contact_form_view, success_page

urlpatterns = [
    path('', contact_form_view, name='contact_form'),
    path('success/', success_page, name='success_page'),
]
