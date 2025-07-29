from django.urls import path
from .views import ListCreateApi, DetailUpdateDeleteApi
urlpatterns = [
    # path('', book_list, name='list'),
    # path('detail/<int:pk>/', book_detail, name='detail'),
    # path('create/', book_create, name='create'),
    # path('update/<int:pk>/', book_update, name='update'),
    # path('delete/<int:pk>/', book_delete, name='delete'),
    
    path('', ListCreateApi.as_view(), name='list'),
    path('u/<int:pk>/', DetailUpdateDeleteApi.as_view()),

]


