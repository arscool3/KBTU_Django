import dataclasses

from django.shortcuts import render


@dataclasses.dataclass
class User:
    name: str
    age: int
    gender: str


users = [
    User("John", 27, "male"),
    User("Jane", 66, "female"),
    User("Mike", 19, "female"),
    User("David", 8, "female"),
    User("John", 33, "female"),
    User("Mike", 5, "female"),
    User("David", 78, "male"),
]


def index(request):
    return render(request, 'index.html', {
        'users': users
    })
