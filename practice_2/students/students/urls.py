from django.contrib import admin
from django.urls import path
from students import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.student_list, name='student_list'),
    
]