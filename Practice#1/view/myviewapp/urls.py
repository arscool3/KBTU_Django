from django.urls import path
from . import views

urlpatterns = [
    path('main/' , views.main_view, name= 'main-view'),
    path('basic/' , views.basic_view , name= 'basic-view'),
    path('test/' , views.test_view , name= 'test-view'),

]