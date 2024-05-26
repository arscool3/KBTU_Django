
# noinspection PyUnresolvedReferences
from api.models.userlist import UserList
# noinspection PyUnresolvedReferences
from api.serializers.category import CategorySerializer2
from rest_framework import serializers
from django.contrib.auth.models import User
# noinspection PyUnresolvedReferences
from api.models.userlist import UserList
# noinspection PyUnresolvedReferences
from api.serializers.category import CategorySerializer2
from rest_framework import serializers
from django.contrib.auth.models import User
# noinspection PyUnresolvedReferences
from api.serializers.book import BookSerializer2


class ListSerializer1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    user = User
    books = BookSerializer2(many=True)


class ListSerializer2(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ('id', 'name', 'user', 'books', )

    
    