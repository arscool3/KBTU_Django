from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    website = models.URLField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # city = models.CharField(max_length=100)
    # country = models.CharField(max_length=100)

    def __str__(self):
        return "#{}: {}".format(self.id, self.name)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.email


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    num_pages = models.IntegerField(default=10)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
