from rest_framework import serializers

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
  #      model = YourModel
        fields = '__all__'  


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
      #  model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested serializer for author
    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')  # ManyToMany with Category

    class Meta:
      #  model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'categories']