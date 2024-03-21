from django.urls import path
from . import views

urlpatterns = [
    path('view1/', views.viewshka1),
    path('view2/', views.viewshka2),
    path('view3/', views.viewshka3),
]