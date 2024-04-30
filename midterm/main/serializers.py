from rest_framework import serializers

from main.models import Author, Book, Category, Consumer, Review

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = '__all__'

class ConsumerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Consumer
    fields = '__all__'