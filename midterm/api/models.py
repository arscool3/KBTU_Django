import bcrypt
from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Group(models.Model):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.name}'


class User(models.Model):

    username = models.CharField(max_length=50, unique=True)

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_verified = models.BooleanField(default=True, blank=True)

    def set_password(self, password):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def generate_username(self, name, surname):
        users = User.objects.filter(name=name, surname=surname)
        if len(users) < len(name):
            result = name[0:len(users) + 1].lower() + "_" + surname.lower()
        else:
            result = name[0].lower() + "_" + surname.lower() + str(len(users) - len(name) + 1)
        self.username = result

    def __str__(self):
        return f'{self.id}: {self.name}, {self.role}, {self.group}, {self.organization}'


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.name}, {self.organization}'


class Events(models.Model):
    discipline = models.CharField(max_length=150)
    event_start_time = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    day = models.IntegerField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f'{self.id}: {self.discipline}, {self.event_start_time}, {self.day}, {self.room.name}, {self.tutor}'