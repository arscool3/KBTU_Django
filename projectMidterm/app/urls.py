from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    
    path('filter-by-trainer/', views.filter_workouts_by_trainer, name='filter_workouts_by_trainer'),
    path('filter-by-type/', views.filter_workouts_by_type, name='filter_workouts_by_type'),
    
    path('api/members/', views.get_all_members, name='get_all_members'),
    path('api/members/<int:id>/', views.get_member_details, name='get_member_details'),
    path('api/members/add/', views.add_member, name='add_member'),
    
    path('api/trainers/', views.get_all_trainers, name='get_all_trainers'),
    path('api/trainers/<int:id>/', views.get_trainer_details, name='get_trainer_details'),
    path('api/trainers/add/', views.add_trainer, name='add_trainer'),
    

    # Filter endpoints
    path('filter-by-trainer/', views.filter_workouts_by_trainer, name='filter_workouts_by_trainer'),
    path('filter-by-type/', views.filter_workouts_by_type, name='filter_workouts_by_type'),

    # Members endpoints
    path('api/members/', views.get_all_members, name='get_all_members'),
    path('api/members/<int:id>/', views.get_member_details, name='get_member_details'),
    path('api/members/add/', views.add_member, name='add_member'),

    # Trainers endpoints
    path('api/trainers/', views.get_all_trainers, name='get_all_trainers'),
    path('api/trainers/<int:id>/', views.get_trainer_details, name='get_trainer_details'),
    path('api/trainers/add/', views.add_trainer, name='add_trainer'),

    # Workouts endpoints

    path('api/workouts/', views.get_all_workouts, name='get_all_workouts'),
    path('api/workouts/<int:id>/', views.get_workout_details, name='get_workout_details'),
    path('api/workouts/add/', views.add_workout, name='add_workout'),



    # Membership plans endpoints
    path('api/memberships/', views.get_all_membership_plans, name='get_all_membership_plans'),
    path('api/memberships/<int:id>/', views.get_membership_plan_details, name='get_membership_plan_details'),
    path('api/memberships/add/', views.add_membership_plan, name='add_membership_plan'),
]
