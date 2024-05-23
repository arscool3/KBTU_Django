from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InstructorViewSet, MemberViewSet, GymViewSet, MembershipViewSet, EquipmentViewSet, WorkoutViewSet,
    index, about, add_instructor, add_member, add_gym, add_membership, add_equipment, add_workout,
    filter_instructors, filter_gyms, register, custom_logout, get_members, get_gyms, get_memberships, get_equipment, get_workouts, show_instructor, delete_instructor
)
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'instructors', InstructorViewSet)
router.register(r'members', MemberViewSet)
router.register(r'gyms', GymViewSet)
router.register(r'memberships', MembershipViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('', index, name='mainpage'),
    path('about/', about, name='aboutpage'),
    path('add_instructor/', add_instructor, name='add_instructor'),
    path('add_member/', add_member, name='add_member'),
    path('add_gym/', add_gym, name='add_gym'),
    path('add_membership/', add_membership, name='add_membership'),
    path('add_equipment/', add_equipment, name='add_equipment'),
    path('add_workout/', add_workout, name='add_workout'),
    path('filter/instructors/', filter_instructors, name='filter_instructors'),
    path('filter/gyms/', filter_gyms, name='filter_gyms'),
    path('accounts/register/', register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='main/registration/login.html'), name='login'),
    path('accounts/logout/', custom_logout, name='logout'),
    path('instructors/<int:pk>/', show_instructor, name='show_instructor'),
    path('instructors/<int:pk>/delete/', delete_instructor, name='delete_instructor'),
    path('', include(router.urls)),  # Include the DRF router URLs
]

urlpatterns += router.urls
