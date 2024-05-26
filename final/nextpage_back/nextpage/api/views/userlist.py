import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# noinspection PyUnresolvedReferences
from api.serializers.category import CategorySerializer2
# noinspection PyUnresolvedReferences
from api.serializers.book import BookSerializer2
# noinspection PyUnresolvedReferences
from api.models.category import Category
# noinspection PyUnresolvedReferences
from api.models.book import Book
# noinspection PyUnresolvedReferences
from api.models.userlist import UserList
from django.contrib.auth.models import User
# noinspection PyUnresolvedReferences
from api.serializers.book import BookSerializer2
# noinspection PyUnresolvedReferences
from api.models.category import Category
# noinspection PyUnresolvedReferences
from api.models.book import Book
# noinspection PyUnresolvedReferences
from api.models.userlist import UserList
from django.contrib.auth.models import User
# noinspection PyUnresolvedReferences
from api.serializers.userlist import ListSerializer2



class UserListAPI(APIView):
    


    def get(self, request, user_id, list_id):
        userlist = UserList.objects.get(pk=list_id)
        serializer = ListSerializer2(userlist)
        return Response(serializer.data)


class UserListDetailAPI(APIView):
    def get(self, request,  list_id):
        user_id = request.user
        # return JsonResponse({user_id:99})
        userlist = UserList.objects.get(pk=list_id)
        serializer = ListSerializer2(userlist)
        return Response(serializer.data)
    
class GetUsersListsAPI(APIView):
    def getListObject(self, user):
        try:
            return UserList.objects.filter(user=user)
        except UserList.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        userlists = self.getListObject(user)
        serializer = ListSerializer2(userlists, many=True)
        return Response(serializer.data)
    

class BookOneUserListAPI(APIView):
    def getListObject(self, list_name, user):
        try:
            return UserList.objects.get(name=list_name, user=user)
        except User.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
    def getBook(self, id):
        try:
            return Book.objects.get(pk=id)
        except Book.DoesNotExist as e:
            return HttpResponse(status=404)

    def get(self, request, list_name):
        user = request.user
        userlist = self.getListObject(list_name, user)
        books = userlist.books.all()
        # if (books.count()==0):
        #     return JsonResponse({"not":"found"})
        # else:
            
        serializer = BookSerializer2(books, many=True)
        #     serializer = ListSerializer2(userlist)
        return Response(serializer.data)
    def post(self, request, list_name):
        data = json.loads(request.body)

        book_id = data.get('book','')
        book = self.getBook(book_id)
        user = request.user
        userlist = self.getListObject(list_name, user)
        userlist.books.add(book)
        userlist.save()
        serializer = ListSerializer2(userlist)
        return Response(serializer.data)
    
    def delete(self, request, list_name) :
        data = json.loads(request.body)
        book_id = data.get('book','')
        book = self.getBook(book_id)
        user = request.user
        userlist = self.getListObject(list_name, user)
        userlist.books.remove(book)
        serializer = ListSerializer2(userlist)
        return Response(serializer.data)



class ListOfBook(APIView):
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        ulist = book.userlist_set.all()
        serializer = ListSerializer2(ulist, many=True)
        return Response(serializer.data)
    

class BookOneOtherListAPI(APIView):
    def getListObject(self, list_name, user):
        try:
            return UserList.objects.get(name=list_name, user=user)
        except User.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
    def getBook(self, id):
        try:
            return Book.objects.get(pk=id)
        except Book.DoesNotExist as e:
            return HttpResponse(status=404)

    def get(self, request, list_name, user_id):
        user = User.objects.get(pk=user_id)
        userlist = self.getListObject(list_name, user)
        books = userlist.books.all()

        # if (books.count()==0):
        #     return JsonResponse({"not":"found"})
        # else:

        if (books.count()==0):
            return Response(books)
        else:
            
                serializer = BookSerializer2(books, many=True)
        #     serializer = ListSerializer2(userlist)
                return Response(serializer.data)
    