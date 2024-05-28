from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EventViewSet, ParticipantViewSet, OrganizerViewSet, TicketViewSet, SponsorViewSet, ProfileViewSet, login_view, logout_view
from django.contrib.auth import views as auth_views
from .views import register_user



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'events', EventViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'organizers', OrganizerViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'sponsors', SponsorViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', register_user, name='register')
]

urlpatterns = [] + router.urls