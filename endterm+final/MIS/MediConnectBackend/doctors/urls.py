from django.urls import path
from .views import DoctorListView, DoctorDetailView, DoctorAppointmentListView, DoctorAppointmentDetailView, AppointmentDetailView, VerifyDoctorLicenseView, get_profile_id_by_doctor_id, AppointmentUpdateGoogleMeetLinkView

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctor-appointments/<int:doctor_profile_id>/', DoctorAppointmentListView.as_view(), name='doctor-appointment-list'),
    path('doctor-appointments/<int:profile_id>/detail/<int:pk>/', DoctorAppointmentDetailView.as_view(), name='doctor-appointment-detail'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('doctor_profile_id/<int:doctor_id>/', get_profile_id_by_doctor_id, name='doctor_profile_id'),
    path('verify-doctor-license', VerifyDoctorLicenseView.as_view(), name='verify-doctor-license'),
    path('appointments/<int:pk>/update-google-meet-link/', AppointmentUpdateGoogleMeetLinkView.as_view(), name='appointment-update-google-meet-link'),
]
