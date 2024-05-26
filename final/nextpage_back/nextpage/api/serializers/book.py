# noinspection PyUnresolvedReferences
from api.models.book import Book
# noinspection PyUnresolvedReferences
from api.serializers.category import CategorySerializer2
from rest_framework import serializers

class BookSerializer1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    img = serializers.CharField()
    pages = serializers.FloatField()
    category = CategorySerializer2()


class BookSerializer2(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(source='get_category_name')
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'description', 'img', 'pages', 'category','category_name',)
    def get_category_name(self, obj):
        return obj.category.name
    