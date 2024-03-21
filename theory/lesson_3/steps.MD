> Initially you have something like that 
>
> If not, check previous lessons


```
├── manage.py
├── test_app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── test_project
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-310.pyc
    │   └── settings.cpython-310.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```


### Now you need to create templates folder inside your application
*Inside templates directory you need to create .html file*
*Paste some html + jinja content there*

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

> Here {% %} and {{ }} are some of jinja syntax, check [more](https://jinja.palletsprojects.com/en/3.1.x/*)

### after that, you obviously need to transfer some students here

1. Create views.py
2. write some code
3. that's all

### example

```python
def view(request):
    return render(request, 'index.html', {'students': students})
```

### Now you only need to use this view inside your urls

> Thank you !