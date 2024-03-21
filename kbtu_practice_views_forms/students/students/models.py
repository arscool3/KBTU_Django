from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
        
    def __str__(self):
        return f'{self.id}: {self.name}: {self.address}: {self.email} : {self.phone}'
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'email': self.email,
            'phone': self.phone
        }

    