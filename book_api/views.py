from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.http import HttpResponse

from book_api.models import Book
from book_api.serializer import BookSerializer
@api_view(['POST','GET'])
def books(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == "GET":
            book = Book.objects.all()
            serializer = BookSerializer(book, many=True)
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def book(request, id):
    try:
        book = Book.objects.get(pk =id)
    except:
        return Response("Book not found",status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        try:
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response("Book not found",status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "DELETE":
        try:
            book.delete()
            return Response("Book deleted")
        except:
            return Response("Book not found",status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        try:
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except:
            return Response("Book not found",status=status.HTTP_404_NOT_FOUND)
