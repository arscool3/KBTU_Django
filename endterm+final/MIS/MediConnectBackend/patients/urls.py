from django.urls import path
from .views import PatientListView, PatientDetailView, PatientMedicalRecordDetailView, PatientAppointmentListView, GetPatientIdByProfileIdView

urlpatterns = [
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patients/<int:profile_id>/appointments', PatientAppointmentListView.as_view(), name='patient-appointments'),
    path('patients/medical-records/<int:pk>/', PatientMedicalRecordDetailView.as_view(), name='medical-record-detail'),
    path('patients/profile_id/<int:profile_id>/', GetPatientIdByProfileIdView.as_view(), name='get-patient-id-by-profile-id'),
]
