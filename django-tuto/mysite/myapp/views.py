from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

class BookDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT, safe=False)