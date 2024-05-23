from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MedicalService(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
