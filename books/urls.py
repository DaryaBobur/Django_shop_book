from django.urls import path

from books.views import (CategoryListView, CategoryDetailView, CategoryCreateView,
                         CategoryUpdateView, CategoryDeleteView, BookListView, BookDetailView, BookCreateView,
                         BookUpdateView, BookDeleteView,
                         )

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<slug:slug>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<slug:slug>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/add/', BookCreateView.as_view(), name='book_create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
]
