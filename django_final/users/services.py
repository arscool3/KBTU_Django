import random
import uuid
from typing import Protocol, OrderedDict

from django.contrib.auth.hashers import check_password
from django.core.cache import cache
from django.core.mail import send_mail

from src import settings
from users import repos
from users.models import User
from rest_framework_simplejwt import tokens


class EmailSenderInterface(Protocol):
    @staticmethod
    def send_verify_letter(name: str, surname: str, email: str, code: str): ...

    @staticmethod
    def send_confirmation_letter(user: User): ...


class EmailSender:
    @staticmethod
    def send_verify_letter(name: str, surname: str, email: str, code: str):
        send_mail(
            "Please enter code on the website",
            f"Here is your code: {code}",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

    @staticmethod
    def send_confirmation_letter(user: User):
        send_mail(
            "Successfully registered",
            "Thanks for registering on our canteen app",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )


class UserServicesInterface(Protocol):
    def create_user(self, data: OrderedDict) -> str: ...

    def verify_user(self, data: OrderedDict) -> User: ...

    def create_token(self, data: OrderedDict) -> str: ...

    def verify_token(self, data: OrderedDict) -> dict: ...

    def get_user(self, data: OrderedDict) -> User: ...

    def update_user(self, data: OrderedDict, user_id: str) -> User: ...


class UserServicesV1:
    user_repos: repos.UserReposInterface = repos.UserReposV1()
    email_sender: EmailSenderInterface = EmailSender()

    def create_user(self, data: OrderedDict) -> str:
        return self._verify_email(data=data)

    def get_user(self, data: OrderedDict) -> User:
        payload = tokens.AccessToken(data['access_token']).payload
        user_id = payload.get('user_id')

        return self.user_repos.get_user(data={'id': user_id})

    def update_user(self, data: OrderedDict, user_id: str):
        user = self.user_repos.get_user(data={'id': user_id})
        print(user)
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.email = data["email"]
        user.save()

        return user

    def verify_user(self, data) -> User:
        user_data = cache.get(data['session_id'])
        if user_data['code'] == data['code']:
            user = self.user_repos.create_user(data={
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'email': user_data['email'],
                'password': user_data['password'],
            })

            self.email_sender.send_confirmation_letter(user=user)
            return user
        return None

    def create_token(self, data: OrderedDict):
        user = self.user_repos.get_user(data={'email': data['email']})

        if not user:
            return None

        if check_password(password=data['password'], encoded=user.password):
            access = tokens.AccessToken.for_user(user)
            refresh = tokens.RefreshToken.for_user(user)

            return {
                'access': str(access),
                'refresh': str(refresh),
            }

    def verify_token(self, data: OrderedDict) -> dict:
        user_data = cache.get(data['session_id'])

        user = self.user_repos.get_user(data={'email': user_data['email']})

        access = tokens.AccessToken.for_user(user)
        refresh = tokens.RefreshToken.for_user(user)

        return {
            'access': str(access),
            'refresh': str(refresh),
        }

    def _verify_email(self, data: OrderedDict) -> str:
        code = self._generate_code()
        session_id = self._generate_session_id()
        cache.set(session_id, {**data, 'code': code}, timeout=300)

        self.email_sender.send_verify_letter(name=data['first_name'], surname=data['last_name'], email=data['email'], code=code)

        return session_id

    @staticmethod
    def _generate_code() -> str:
        return ''.join(random.choices([str(i) for i in range(10)], k=4))

    @staticmethod
    def _generate_session_id() -> str:
        return str(uuid.uuid4())
