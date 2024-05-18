from django.db import models
from django.contrib.auth.models import User
from authen.models import Profile
from patients.models import Patient
from services.models import Specialty

class Doctor(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, null=True)
    clinic_location = models.CharField(max_length=255, blank=True, null=True)
    iin_bin = models.CharField(max_length=12, blank=True, null=True)
    license_number = models.CharField(max_length=100, blank=True, null=True)
    license_issued_date = models.DateField(null=True, blank=True)
    license_status = models.CharField(max_length=100, default='Not Verified', choices=[
        ('Not Verified', 'Not Verified'),
        ('Pending Verification', 'Pending Verification'),
        ('Verified', 'Verified'),
        ('Rejected', 'Rejected')
    ])

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(null=True, blank=True)
    google_meet_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Appointment with {self.doctor} at {self.date_and_time}"
