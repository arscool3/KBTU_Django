from django.db import models


class Base(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class University(Base):
    build_year = models.IntegerField()
    popular = models.BooleanField(default=False)


class Faculty(Base):
    relevant = models.BooleanField(default=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class Speciality(Base):
    code = models.CharField(max_length=10)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Student(Base):
    id = models.UUIDField
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)