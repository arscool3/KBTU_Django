# Intro

Hello, this is my midterm project. I have wondered how it would be
to create a social media. I have tried it two times in the past.
But the attempts to build it were not successful(Only the one which was made in Spring application was fine enough, but was still raw).

p.s. WebSocket is still so fun :)

Furthermore, I choose 'scoial media' as a topic of the midterm.

**The main source where I will find help is: *https://www.geeksforgeeks.org/***

Let's start

# Project requirements

#### 1. Django
#### 2. Django channels (to enable async programming and WebSocket)
    python -m pip install -U channels

Note : Starting from version 4.0.0 of channels, ASGI runserver in development mode does not work anymore. You will have to install daphne as well.

    python -m pip install -U daphne

# Adding dependencies
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',
    'django.contrib.staticfiles',
    'api',
    'channels'
]
....
ASGI_APPLICATION = 'midterm.asgi.application'
```

