from django.db import models
from django.db.models import TextChoices


# Create your models here.


class Base(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class DragonSize(TextChoices):
    SMALL = 'small', 'Small'
    MEDIUM = 'medium', 'Medium'
    LARGE = 'large', 'Large'


class UnitManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().order_by('-attack')

    # def armor(self):
    #     return super().get_queryset().order_by('-armor')


class Unit(Base):
    health = models.IntegerField()
    mana = models.IntegerField()
    attack = models.IntegerField()
    armor = models.IntegerField()
    objects = UnitManager()


class ClanManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-level')


class Clan(Base):
    level = models.IntegerField()
    objects = ClanManager()


class CastleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-population')


class Castle(Base):
    location = models.CharField(max_length=100)
    population = models.IntegerField()
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE)
    objects = CastleManager()


class Hero(Unit):
    castle = models.ForeignKey(Castle, on_delete=models.CASCADE)


class Dragon(Unit):
    size = models.CharField(max_length=30, choices=DragonSize.choices)


class NPC(Base):
    castle = models.ForeignKey(Castle, on_delete=models.CASCADE)


