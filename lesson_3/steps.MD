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
│   ├── templates
│   │   └── index.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py

```


### Now you need to create templatetags folder inside your application
*Inside templatetags directory you need to create some filters for using them inside templates*

*Exmaple for capitalizing letter inside html* 

```python
from django import template

register = template.Library()


@register.filter
def capitalize(value: str) -> str:
    return value.capitalize()

```

### after that, you obviously need to use it inside html like that

1. Load this file (my file is utils.py so I load utils)
2. write some code (use filter wiht | syntax)
3. that's all

### example

```html
{% load utils %}

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
    <h3>Students</h3>
    <ul>
        {% for student in students %}
            <li>My name is {{student.name| capitalize}}, age = {{student.age}}, sex = {{student.sex}}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Now you only need to use this template inside your view

> Thank you !