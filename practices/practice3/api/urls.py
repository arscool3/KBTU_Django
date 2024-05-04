from django.urls import path
from .views import studentVIew, home


urlpatterns = [
    path('student/', studentVIew, name='student'),
    path('', home, name='home'),
]