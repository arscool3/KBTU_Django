from django.db import models
from random import randint

# Create your models here.
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

names = ['Shaylee', 'Elliott',
'David', 'Curtis',
'Kayden', 'Banks',
'Naima', 'Kent',
'Britney', 'Freeman',
'Addisyn', 'Hopkins',
'Bridget', 'Melendez',
'Dakota', 'Lyons',
'Leyla','Serrano',
'Kian', 'Pratt',
'Brycen', 'Combs',
'Chance', 'Powers']

student_list = [Student(f'{names[randint(0, 23)]}', f'{names[randint(0, 23)]}') for val in range(20)]