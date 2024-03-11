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

# class UnitQuerySet(models.QuerySet):
#
#     def get_units

class Unit(Base):
    health = models.IntegerField(default=100)
    damage = models.IntegerField(default=10)
    armor = models.IntegerField(default=0)
    objects = UnitManager()

class Weapon(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    weapon_type = models.CharField(max_length=30)
    units = models.ManyToManyField(Unit)
    damage = models.IntegerField(default=20)


class PlayerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-score')

class Player(Base):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    team = models.CharField(max_length=30)  # 'Terrorist' or 'Counter-Terrorist'
    objects = PlayerManager()


class Map(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)


class GameQueryset(models.QuerySet):

    def get_game_by_map(self, map_name):
        return self.filter(map__name=map_name)


class CounterStrikeGame(models.Model):
    # This model represents the entire Counter-Strike game
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    map = models.OneToOneField(Map, on_delete=models.CASCADE)
    objects = GameQueryset.as_manager()


class Terrorist(Player):
    weapon = models.ManyToManyField(Weapon)
    game = models.ForeignKey(CounterStrikeGame, on_delete=models.CASCADE)
    main_weapon = models.CharField(max_length=30, default='AK-47')
    bomb_in_the_inventory = models.BooleanField(default=False)


class BombQueryset(models.QuerySet):
    def get_planted_terrorist(self):
        return self.select_related('planted_by')

class Bomb(Base):
    location = models.CharField(max_length=100)
    planted_by = models.ForeignKey(Terrorist, on_delete=models.CASCADE, related_name='planted_bombs')
    objects = BombQueryset.as_manager()

    def __str__(self):
        return f"Bomb at {self.location} planted by {self.planted_by}"



class CounterTerrorist(Player):
    game = models.ForeignKey(CounterStrikeGame, on_delete=models.CASCADE)
    weapon = models.ManyToManyField(Weapon)
    main_weapon = models.CharField(max_length=30, default='M4A4')


class Hostage_or_Bot(Unit):
    weapon = models.ManyToManyField(Weapon)
    main_weapon = models.CharField(max_length=30, default='AUG')