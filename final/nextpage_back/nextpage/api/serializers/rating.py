# noinspection PyUnresolvedReferences
from api.models.rating import Rating
# noinspection PyUnresolvedReferences
from api.serializers.book import BookSerializer2
from rest_framework import serializers

class RatingSerializer1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    count = serializers.IntegerField()
    sum = serializers.IntegerField()
    book = BookSerializer2()


class RatingSerializer2(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField(source='get_book_title')
    class Meta:
        model = Rating
        fields = ('id', 'count','sum', 'book', 'book_title',)
    def get_book_title(self, obj):
        return obj.book.title