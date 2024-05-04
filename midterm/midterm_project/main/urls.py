from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='mainpage'),
    path('about/', views.about, name='aboutpage'),
    path('instructors/', views.instructor_list, name='get_instructors'),
    path('members/', views.member_list, name='get_members'),
    path('gyms/', views.gym_list, name='get_gyms'),
    path('memberships/', views.membership_list, name='get_memberships'),
    path('equipment/', views.equipment_list, name='get_equipment'),
    path('workouts/', views.workout_list, name='get_workouts'),
    path('add_instructor/', views.add_instructor, name='add_instructor'),
    path('add_member/', views.add_member, name='add_member'),
    path('add_gym/', views.add_gym, name='add_gym'),
    path('add_membership/', views.add_membership, name='add_membership'),
    path('add_equipment/', views.add_equipment, name='add_equipment'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('filter/instructors/', views.filter_instructors, name='filter_instructors'),
    path('filter/gyms/', views.filter_gyms, name='filter_gyms'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='main/registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='main/registration/logout.html'), name='logout'),
    path('instructors/<int:pk>/', views.show_instructor, name='show_instructor'),
    path('instructors/<int:pk>/delete/', views.delete_instructor, name='delete_instructor'),
]
