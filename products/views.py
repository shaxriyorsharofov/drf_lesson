from django.shortcuts import render
from .models import Books
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

    
# Create your views here


# @api_view(['GET', ])
# def book_list(request):
#     book = Books.objects.all()
#     serializer = BookSerializer(book, many=True)
#     res = {
#         'data': serializer.data,
#         'count':len(book),
#         'status':status.HTTP_200_OK,
#     }
#     return Response(res)

# class BookList(ListCreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer



# @api_view(['GET', ])
# def book_detail(request, pk):
#     try:
#         book = Books.objects.get(id=pk)
#     except Books.DoesNotExist:
#         return Response({'status': status.HTTP_400_BAD_REQUEST})
#     serializer = BookSerializer(book)
#     return Response({
#         'book': serializer.data,
#         'status': status.HTTP_200_OK
#     })
    
# class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
    
# @api_view(['POST', ])
# def book_create(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status': status.HTTP_201_CREATED})
#     return Response({'status': status.HTTP_400_BAD_REQUEST, 'error': serializer.errors})

# @api_view(['PATCH',])
# def book_update(request, pk):
#     try: 
#         book = Books.objects.get(id=pk)
#     except Books.DoesNotExist:
#         return Response({'error': 'Book not found', 'status': status.HTTP_404_NOT_FOUND})
    
#     serializer = BookSerializer(book, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status': status.HTTP_200_OK})
#     return Response({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})


# @api_view(['DELETE',])
# def book_delete(request, pk):
#     try: 
#         book = Books.objects.get(id=pk)
#     except Books.DoesNotExist:
#         return Response({'error': 'Book not found', 'status': status.HTTP_404_NOT_FOUND})
#     book.delete()
#     return Response({'info': "ochirildi", 'status': status.HTTP_200_OK})   
        

# class BookApiView(APIView):
#     def get(self, request):
#         book = Books.objects.all()
#         serializer = BookSerializer(book, many=True)
#         data = {
#             'books': serializer.data,
#             'status': status.HTTP_200_OK,
#             'count': len(book)
#         }
#         return Response(data)
        
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': "created book", 'status':status.HTTP_201_CREATED})
#         return Response({'error': serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})



class ListCreateApi(GenericAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
    def get(self,  request):
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        data = {
            'data': serializer.data,
            'count': len(books),
            'status': status.HTTP_200_OK
        }
        
        return Response(data)
    
    
class DetailUpdateDeleteApi(GenericAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
    def get_object(self, pk):
        book = Books.objects.get(id=pk)
        return book
    
    def get(self, request, pk):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(book)
        data = {
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }
        
        return Response(data)
        
    