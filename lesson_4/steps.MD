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


### Now you need to create your first model inside models.py
*Example*

```python
class Person(models.Model):
    name = models.CharField(max_length=20)
```

> You also need to migrate your models inside db
> 
> python3 manage.py makemigations
> 
> python3 manage.py migrate


### You also want to add this model inside you admin page /admin

*Inside admin.py*

```python
from django.contrib import admin

from core.models import Person

admin.site.register(Person)
```

### And add form for creation this model (Person)

*Inside forms.py*

```python
from django import forms

from core.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
```

### Certainly, some template

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
     <form action="{% url person %}" method="post">
         {% csrf_token %}
         {{form}}
     <input type="submit" value="Submit">
     </form>
</body>
</html>
```


### Now, you only need use it logic inside your view

```python
def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, person was created')

    return render(request, 'index.html', {'form': PersonForm())
```

### After you added your instances inside db, you can check it via admin page (/admin)
you need to create superuser
> python3 manage.py createsuperuser


### That's all. Thank you

### LINKS

> https://docs.djangoproject.com/en/5.0/topics/db/models/
> https://docs.djangoproject.com/en/5.0/topics/forms/