*Install Django*

> pip install django

*Create Django Project*

> django-admin startproject "project_name"

```
You will have this structure

├── manage.py
└── test_project
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```

*Run server*

> python3 manage.py runserver

Create You First Django Application*

> python3 manage.py startapp "application_name"

```
You will have this structure

├── db.sqlite3
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
    │   ├── settings.cpython-310.pyc
    │   ├── urls.cpython-310.pyc
    │   └── wsgi.cpython-310.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```

> You just need to add urls.py in your application

> Check all examples practice folders
