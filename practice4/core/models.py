from django.db import models
from django.db.models import TextChoices


class Base(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class UnitManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-health')

class Unit(Base):
    health = models.IntegerField(default=100)
    damage = models.IntegerField(default=10)
    init_weapon = models.CharField(max_length=30)
    armor = models.IntegerField(default=0)
    objects = UnitManager()


class PlayerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-score')

class Player(Base):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    team = models.CharField(max_length=30)  # 'Terrorist' or 'Counter-Terrorist'
    objects = PlayerManager()

class Bomb(Base):
    location = models.CharField(max_length=100)
    planted_by = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='planted_bombs')


class CounterStrikeGame(models.Model):
    # This model represents the entire Counter-Strike game
    name = models.CharField(max_length=100)
    map_name = models.CharField(max_length=100)


class Terrorist(Player):
    game = models.ForeignKey(CounterStrikeGame, on_delete=models.CASCADE)
    main_weapon = models.CharField(max_length=30, default='AK-47')


class CounterTerrorist(Player):
    game = models.ForeignKey(CounterStrikeGame, on_delete=models.CASCADE)
    main_weapon = models.CharField(max_length=30, default='M4A4')

class Hostage_or_Bot(Unit):
    pass

