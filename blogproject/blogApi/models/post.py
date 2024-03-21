from django.db import models
from blogApi.models.category import Category

class Post(models.Model):
    title = models.CharField('Заголовок записи', max_length=400)
    description= models.TextField('Текст записи')
    date = models.DateField('Дата Публикации')
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"
    