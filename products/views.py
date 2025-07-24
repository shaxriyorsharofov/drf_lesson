from django.shortcuts import render
from .models import Books
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', ])
def book_list(request):
    book = Books.objects.all()
    serializer = BookSerializer(book, many=True)
    res = {
        'data': serializer.data,
        'count':len(book),
        'status':status.HTTP_200_OK,
    }
    return Response(res)
