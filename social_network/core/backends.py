import jwt

from django.conf import settings

from rest_framework import authentication, exceptions

from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Bearer'

    def authenticate(self, request):
        """
        Метод authenticate вызывается каждый раз, независимо от того, требует
        ли того эндпоинт аутентификации. 'authenticate' имеет два возможных
        возвращаемых значения:
            1) None - мы возвращаем None если не хотим аутентифицироваться.
            Обычно это означает, что мы значем, что аутентификация не удастся.
            Примером этого является, например, случай, когда токен не включен в
            заголовок.
            2) (user, token) - мы возвращаем комбинацию пользователь/токен
            тогда, когда аутентификация пройдена успешно. Если ни один из
            случаев не соблюден, это означает, что произошла ошибка, и мы
            ничего не возвращаем. В таком случае мы просто вызовем исключение
            AuthenticationFailed и позволим DRF сделать все остальное.
        """
        request.user = None

        # 'auth_header' должен быть массивом с двумя элементами:
        # 1) именем заголовка аутентификации (Token в нашем случае)
        # 2) сам JWT, по которому мы должны пройти аутентифкацию
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            # Некорректный заголовок токена, в заголовке передан один элемент
            return None

        elif len(auth_header) > 2:
            # Некорректный заголовок токена, какие-то лишние пробельные символы
            return None

        # JWT библиотека которую мы используем, обычно некорректно обрабатывает
        # тип bytes, который обычно используется стандартными библиотеками
        # Python3 (HINT: использовать PyJWT). Чтобы точно решить это, нам нужно
        # декодировать prefix и token. Это не самый чистый код, но это хорошее
        # решение, потому что возможна ошибка, не сделай мы этого.
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            # Префикс заголовка не тот, который мы ожидали - отказ.
            return None

        # К настоящему моменту есть "шанс", что аутентификация пройдет успешно.
        # Мы делегируем фактическую аутентификацию учетных данных методу ниже.
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
        Попытка аутентификации с предоставленными данными. Если успешно -
        вернуть пользователя и токен, иначе - сгенерировать исключение.
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except Exception:
            msg = 'Ошибка аутентификации. Невозможно декодировать токеню'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'Пользователь соответствующий данному токену не найден.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'Данный пользователь деактивирован.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)