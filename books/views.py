from django.shortcuts import render
from django.db.models import Count, Q
from books.models import Category, Book


def home(request):
    qs = Category.objects.all()
    context = {'object_list': qs}
    return render(request, 'books/categories.html', context)

def books_list(request):
    qs = Book.objects.all()
    context = {'object_list': qs}
    return render(request, 'books/books.html', context)



# Django ORM запити (filter, annotate, Q-об'єкти).
def queries(request):
    all_books = Book.objects.all()
    books_filter = Book.objects.filter(stock = 0)
    books_q = Book.objects.filter(
        Q(price__lt = 500) & Q(stock__gt = 0)
    )
    categories = Category.objects.annotate(
        books_count=Count('book')
    )

    context = {
        'all_books': all_books,
        'books_filter': books_filter,
        'books_q': books_q,
        'categories': categories
    }

    return render(request, 'books/queries.html', context)

