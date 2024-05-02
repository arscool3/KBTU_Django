from django.db import models

class PersonManager(models.QuerySet):
    def get_by_family(self, f_id):
        return self.filter(family_id=f_id)
    def get_by_age(self, age):
        return self.filter(age=age)

    def get_by_id(self, m_id):
        return self.get(id=m_id)

class DoctorManager(models.QuerySet):
    def get_by_hospital(self, h_id):
        return self.filter(work_place_id=h_id)
    def get_by_id(self, m_id):
        return self.get(id=m_id)


class common(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Person(common):
    surname = models.CharField(max_length=255)
    family = models.ForeignKey('Family', on_delete=models.PROTECT, blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    objects = PersonManager().as_manager()

    def __str__(self):
        return self.name


class Family(common):
    doctor = models.ForeignKey('FamilyDoctor', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class FamilyDoctor(models.Model):
    personality = models.ForeignKey('Person', on_delete=models.PROTECT)
    work_place = models.ForeignKey('Hospital', on_delete=models.PROTECT)

    objects = DoctorManager().as_manager()

    def __str__(self):
        return 'doctror ' + self.personality.name


class Hospital(common):
    adress = models.TextField()
    office_phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name