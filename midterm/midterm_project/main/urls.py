from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'mainpage'),
    path('about', views.about, name = 'aboutpage'),
    path('add/Instructor', views.add_instructor, name = 'instructorpage'),
    path('add/Member', views.add_member, name = 'memberpage'),
    path('add/Equipment', views.add_equipment, name = 'equipmentpage'),
    path('add/Gym', views.add_gym, name = 'gympage'),
    path('add/Workout', views.add_workout, name = 'workoutpage'),
    path('add/Membership', views.add_membership, name = 'membershippage'),
    path('filter/instructors', views.filter_instructors, name='filter_instructors'),
    path('filter/gyms', views.filter_gyms, name='filter_gyms'),
    path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register', views.register, name='register')
]