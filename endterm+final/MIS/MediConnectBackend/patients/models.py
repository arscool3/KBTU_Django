from django.db import models
from authen.models import Profile

class Patient(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    
class PatientMedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
