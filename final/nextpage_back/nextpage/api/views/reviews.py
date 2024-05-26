from api.models.review import Review
from rest_framework.views import APIView
from api.models.book import Book
from api.serializers.review import ReviewSerializer2
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from api.models.rating import Rating
from api.serializers.rating import RatingSerializer2
from rest_framework import status
from api.serializers.book import BookSerializer2
from api.serializers.user import UserUpdatingSerializer
import json
@api_view(['GET','POST'])
def reviews(request,id):
    try:
        book = Book.objects.get(id=id)
    except:
        pass
    if request.method == 'GET':
        reviews = Review.objects.filter(book=book).all()
        serializer = ReviewSerializer2(reviews,many=True)
        return Response(
            serializer.data
        )
    if request.method == 'POST':
        data = json.loads(request.body)
        review_review = data.get('review','')
        review_rating = data.get('rating','')
        review_user = User.objects.get(id=data.get('user',''))
        review_book = Book.objects.get(id=data.get('book',''))
        serializerBook = BookSerializer2(review_book,many=False)
        review_book_title = serializerBook.data['title']
        serializerUser = UserUpdatingSerializer(review_user,many=False)
        review = Review.objects.create(review=review_review,rating=review_rating, user=review_user,book=review_book)
        review_data = {'review': review_review,'rating': review_rating, 'user':serializerUser.data,'book':serializerBook.data}
        try:
            ratingBook = Rating.objects.get(book=review_book)
            ratingBook.count += 1
            ratingBook.sum += review_rating
            ratingBook.save()
            serializer = RatingSerializer2(data={'id':ratingBook.id,'count':ratingBook.count,'sum':ratingBook.sum,'book':serializerBook.data,'book_title':ratingBook.book_title})
            if serializer.is_valid():
                serializer.save()
        except:
            ratingBook = Rating.objects.create(count=1,sum=review_rating,book=review_book,book_title=review_book_title)
            serializer = RatingSerializer2(data={'id':ratingBook.id,'count':ratingBook.count,'sum':ratingBook.sum,'book':serializerBook.data,'book_title':ratingBook.book_title})
            if serializer.is_valid():
                serializer.save()
        serializer = ReviewSerializer2(data=review_data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
@api_view(['DELETE'])
def reviewDelete(request,id):
    try:
        review = Review.objects.get(id=id)
        ratingBook = Rating.objects.get(book=review.book)
        ratingBook.count -= 1
        ratingBook.sum -= review.rating
        ratingBook.save()
        serializer = RatingSerializer2(ratingBook,many=False)
        if serializer.is_valid():
            serializer.save()
        review.delete()
        return Response({'deleted': True})
    except:
        return Response({'error'},status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def rating(request,id):
    try:
        book = Book.objects.get(id=id)
    except:
        return Response({'error'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        rating = Rating.objects.get(book=book)
        serializer = RatingSerializer2(rating,many=False)
        return Response(
            serializer.data
        )