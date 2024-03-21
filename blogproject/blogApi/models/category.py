from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return f"{self.name}"