from django.db import models
from django.contrib.auth import get_user_model

from blogApp.models.category import Category

User = get_user_model()

class Post(models.Model):
    title = models.CharField('Заголовок записи', max_length=400)
    description = models.TextField('Текст записи')
    date = models.DateField('Дата Публикации')
    img = models.ImageField('Изображение', upload_to= 'image/%Y')
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    author = User.get_username

    def __str__(self) -> str:
        return f"{self.title}"
    
