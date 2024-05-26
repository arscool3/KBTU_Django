from api.models.review import Review
from api.serializers.book import BookSerializer2
from api.serializers.user import UserUpdatingSerializer
from rest_framework import serializers

class ReviewSerializer1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    review = serializers.CharField()
    rating = serializers.IntegerField()
    book = BookSerializer2()
    user = UserUpdatingSerializer()


class ReviewSerializer2(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField(source='get_book_title')
    user_name = serializers.SerializerMethodField(source='get_user_name')
    class Meta:
        model = Review
        fields = ('id', 'review','rating', 'book', 'book_title','user','user_name')
    def get_book_title(self, obj):
        return obj.book.title
    def get_user_name(self,obj):
        return obj.user.username