from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'mainpage'),
    path('about', views.about, name = 'aboutpage'),
    path('add/instructors', views.add_instructor, name = 'instructorpage'),
    path('add/members', views.add_member, name = 'memberpage'),
    path('add/equipments', views.add_equipment, name = 'equipmentpage'),
    path('add/gyms', views.add_gym, name = 'gympage'),
    path('add/workouts', views.add_workout, name = 'workoutpage'),
    path('add/memberships', views.add_membership, name = 'membershippage'),
    path('filter/instructors', views.filter_instructors, name='filter_instructors'),
    path('filter/gyms', views.filter_gyms, name='filter_gyms'),
    path('accounts/register', views.register, name='register'),
    path('accounts/login', auth_views.LoginView.as_view(template_name='main/registration/login.html'), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='main/registration/logout.html'), name='logout'),

    path('instructors', views.get_instructors, name='get_instructors'),
    path('members', views.get_members, name='get_members'),
    path('gyms', views.get_gyms, name='get_gyms'),
    path('memberships', views.get_memberships, name='get_memberships'),
    path('equipment', views.get_equipment, name='get_equipment'),
    path('workouts', views.get_workouts, name='get_workouts'),

    path('instructors/<int:instructor_id>/', views.show_instructor, name='show_instructor'),
    path('instructors/<int:instructor_id>/delete/', views.delete_instructor, name='delete_instructor'),


]