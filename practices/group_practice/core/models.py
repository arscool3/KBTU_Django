from django.db import models


class SpaceObject(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    radius = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class StarQueryset(models.QuerySet):
    def get_queryset(self):
        return super().order_by('-weight')


class Star(SpaceObject):
    temperature = models.IntegerField()
    objects = StarQueryset.as_manager()


class PlanetQueryset(models.QuerySet):

    def get_planets_by_star_name(self, star_name: str):
        return self.filter(star__name=star_name)

    def get_planets_by_resident_name(self, resident_name: str):
        return self.filter(resident__name=resident_name)

    def habitable(self):
        return self.filter(habitable=True)

    def not_habitable(self):
        return self.filter(habitable=False)


class Planet(SpaceObject):
    habitable = models.BooleanField(default=False)
    star = models.ForeignKey(Star, on_delete=models.CASCADE)
    objects = PlanetQueryset.as_manager()


class SatelliteQueryset(models.QuerySet):

    def get_satellites_by_planet_name(self, planet_name: str):
        return self.filter(planet__name=planet_name)

    def habitable(self):
        return self.filter(habitable=True)

    def not_habitable(self):
        return self.filter(habitable=False)


class Satellite(SpaceObject):
    habitable = models.BooleanField(default=False)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    objects = SatelliteQueryset.as_manager()


class ResidentQueryset(models.QuerySet):

    def get_residents_by_planet_name(self, planet_name: str):
        return self.filter(planet__name=planet_name)


class Resident(models.Model):
    name = models.CharField(max_length=20)
    planet = models.ManyToManyField('Planet')
    objects = ResidentQueryset.as_manager()

    def __str__(self):
        return self.name
