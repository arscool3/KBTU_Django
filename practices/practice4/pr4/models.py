from django.db import models

class CountryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('englishName')
    def area(self):
        return super().get_queryset().order_by('-area')
    def ofname(self):
        return super().get_queryset().order_by('officialName')

class CitizenQuerySet(models.QuerySet):
    def adults(self):
        return self.filter(age__gte=18)
    def kinder(self):
        return self.filter(age__lt=18)

class CitizenManager(models.Manager):
    def get_queryset(self):
        return CitizenQuerySet(self.model, using=self._db)
    def adults(self):
        return self.get_queryset().adults()
    def kinder(self):
        return self.get_queryset().kinder()

class Country(models.Model):
    officialName = models.CharField(max_length=255)
    englishName = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=15, decimal_places=3)
    #president = models.OneToOneField('President', on_delete=models.CASCADE,related_name="pre")
    #population = models.IntegerField()
    objects = CountryManager()
    def __str__(self):
        return self.englishName

class Person(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + " " + self.lname

    class Meta:
        abstract = True

class Citizen(Person):
    city = models.ForeignKey('City', on_delete=models.CASCADE,related_name="res")
    objects = CitizenManager()

class President(Person):
    country = models.OneToOneField('Country', on_delete=models.CASCADE,related_name="sub")

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('Country', on_delete=models.CASCADE,related_name="loc")
    #population = models.IntegerField()
    def __str__(self):
        return self.name
