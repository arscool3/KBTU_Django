from django.db import models

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


class CitizenManager(models.Manager):
    def get_queryset(self):
        return CitizenQuerySet(self.model, using=self._db)

    def criminals(self):
        return self.get_queryset().criminals()

    def not_criminals(self):
        return self.get_queryset().not_criminals()


class Citizen(Base):
    age = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    has_criminal_issues = models.BooleanField(default=False)
    objects = CitizenManager()