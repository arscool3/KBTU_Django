from django.contrib import admin
from django.urls import path
from students import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.add_student, name='add_student'),
]