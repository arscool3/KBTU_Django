> Initially you have something like that 
>
> If not, check previous lessons


```
├── __init__.py
├── db.sqlite3
├── lesson_3
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py

```

### Now we are going to talk about relationships

> For example you have 2 models
2) Country
3) City

> Every country has lots of cities but no city has multiple countries

> So every country has multiple cities

> It is a one to many relationship
 

### Now we are going to code this
```python
class Country(models.Model):
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    population = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=2)

class Citizen(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    has_criminal_issues = models.BooleanField(default=False)

```

we define foreign key for citizen so all citizen have country_id

### Our template will be like this

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h2>{{object}}</h2>
    <ul>
        {% for item in iterable %}
            <li>{{item.name}}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### And views like this

```python
def get_country_by_name(request):
    countries = Country.objects
    if name := request.GET.get('name'):
        countries = countries.filter(name=name.capitalize())
    countries = countries.all()
    return render(request, "index.html", {"iterable": countries, "object": "Countries"})

def get_cities(request):
    cities = City.objects
    if country_name := request.GET.get('country_name'):
        cities = cities.filter(country__name=country_name.capitalize())
    cities = cities.all()
    return render(request, 'index.html', {"iterable": cities, "object": "Cities"})
```

### Also we are going to talk about managers

```python
# so if we use for example Country.objects

# objects it's our manager
# so we can rewrite it inside you models

class CountryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-area')

class Country(Base):
    language = models.CharField(max_length=20)
    population = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=2)
    objects = CountryManager()

so queryset is like you sql query (all filters ordering will be there)

All managers have get_queryset() method
we reload it and return super().get_queryset().order_by(-area)
so now all our countries will always order by area
in the list first country will be the biggest and last one is the smallest
```


### That's all. Thank you

### LINKS

> https://docs.djangoproject.com/en/5.0/topics/db/models/
> https://docs.djangoproject.com/en/5.0/topics/forms/