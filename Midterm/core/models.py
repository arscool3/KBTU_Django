from django.db import models
from django.forms import IntegerField


class Base(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class CountryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-area')


class Country(Base):
    language = models.CharField(max_length=20)
    population = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=2)
    objects = CountryManager()


class City(Base):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class CitizenQuerySet(models.QuerySet):
    def criminals(self):
        return self.filter(has_criminal_issues=True)

    def not_criminals(self):

        return self.filter(has_criminal_issues=False)

    def licence(self):
        return self.filter(has_licence=True)

    def not_licence(self):
        return self.filter(has_licence=False)


# class CitizenManager(models.Manager):
#     def get_queryset(self):
#         return CitizenQuerySet(self.model, using=self._db)
#
#     def criminals(self):
#         return self.get_queryset().criminals()
#
#     def not_criminals(self):
#         return self.get_queryset().not_criminals()
#
#     def licence(self):
#         return self.get_queryset().licence()
#
#     def not_licence(self):
#         return self.get_queryset().not_licence()


class Citizen(Base):
    age = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    has_criminal_issues = models.BooleanField(default=False)
    objects = CitizenQuerySet().as_manager()
    has_licence = models.BooleanField(default=True)


class CarQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def not_active(self):
        return self.filter(is_active=False)

    def get_only_german_cars(self):
        return self.filter(country__name='Germany')

    def get_only_usa_cars(self):
        return self.filter(country__name='USA')

    def get_only_new_cars(self):
        return (car for car in self if car.year > 2015)


# class CarManager(models.Manager):
#     def get_queryset(self):
#         return CarQuerySet(self.model, using=self._db)
#
#     def active(self):
#         return self.get_queryset().active()
#
#     def not_active(self):
#         return self.get_queryset().not_active()


class Car(Base):
    year = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cars')
    carcase = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    objects = CarQuerySet().as_manager()
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE, related_name='cars')

