from django.urls import path
from .views import MedicalServiceListView, MedicalServiceDetailViewByName, SpecialtyListView

urlpatterns = [
    path('services/', MedicalServiceListView.as_view(), name='service-list'),
    path('services/detail', MedicalServiceDetailViewByName.as_view(), name='service-detail'),
    path('specialties/', SpecialtyListView.as_view(), name='specialty-list'),
]
