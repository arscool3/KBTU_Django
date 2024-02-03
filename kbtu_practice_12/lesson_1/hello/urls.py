from django.urls import path

from . import views

urlpatterns = [
    path('mainview/', views.main_view, name='mainview'),
    path('basicview/', views.basic_view, name='basicview'),
    path('testview/', views.test_view, name='testview'),
]
