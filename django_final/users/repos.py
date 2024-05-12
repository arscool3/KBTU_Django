from typing import Protocol, OrderedDict
from .models import User
from rest_framework.generics import get_object_or_404


class UserReposInterface(Protocol):
    @staticmethod
    def create_user(data: dict) -> User: ...

    @staticmethod
    def get_user(data: dict) -> User: ...


class UserReposV1:

    @staticmethod
    def create_user(data: dict) -> User:
        return User.objects.create_user(**data)

    @staticmethod
    def get_user(data: dict) -> User:
        return get_object_or_404(User, **data)
