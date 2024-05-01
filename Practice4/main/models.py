from django.db import models

class Client(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class Manager(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Request(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status_choices = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='pending')

    def __str__(self):
        return self.title

