from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name='index'),
    path('add_model/', add_model),
    path('add_brand/', add_brand),
    path('add_reseller/', add_reseller),
    path('add_showroom/', add_showroom),
    path('reseller/', get_resellers),
    path('model/', get_models),
]