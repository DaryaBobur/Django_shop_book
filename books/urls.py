from django.urls import path
from books.views import home, books_list, queries

urlpatterns = [
    path('category/', home, name='category'),
    path('books/', books_list, name='books'),
    path('queries/',queries,name='queries'),
]