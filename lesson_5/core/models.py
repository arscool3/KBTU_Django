from django.db import models

class Base(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class CountryManager(models.QuerySet):
    # def get_queryset(self):
    #     return super().get_queryset().order_by('-area')

    def get_kaz(self):
        return self.filter(language='kazakh')
    def get_name(self):
        return self.filter(language='kazakh')

class Country(Base):
    language = models.CharField(max_length=20)
    population = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=2)
    objects = CountryManager().as_manager()


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



# Create entire Django Application
# At least 4 models
# At least 2 relationships
# At least 8 methods (4 post, 4 get)
# At least 1 abstract class for models
# At least 2 custom querysets
# At least 6 custom querysets methods