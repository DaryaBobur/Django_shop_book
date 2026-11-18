from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from books.forms import CategoryForm, BookForm
from books.models import Category, Book

class CategoryListView(ListView):
    model = Category
    template_name = 'books/categories.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'books/category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(category=self.object)
        return context


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'books/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('books:category')
    permission_required = "books.add_category"
    raise_exception = True

    def get_success_message(self, cleaned_data):
        message = 'Категорію {name} створено'
        return message.format(**cleaned_data)


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    template_name = 'books/category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('books:category')
    permission_required = "books.change_category"
    raise_exception = True

    def get_success_message(self, cleaned_data):
        message = 'Категорію {name} відредаговано'
        return message.format(**cleaned_data)


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    template_name = 'books/category_delete.html'
    success_url = reverse_lazy('books:category')
    permission_required = "books.delete_category"
    raise_exception = True

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message({'name': self.object.name})

        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        message = 'Категорію {name} видалено'
        return message.format(**cleaned_data)


class BookListView(ListView):
    model = Book
    template_name = 'books/books.html'
    paginate_by = 4

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('category').filter(stock__gt=0)

        title = self.request.GET.get('title', '').casefold()
        if title:
            qs = [
                book for book in qs
                if title in book.title.casefold()
            ]
        return qs


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Book
    template_name = 'books/book_create.html'
    form_class = BookForm
    success_url = reverse_lazy('books:books')
    permission_required = "books.add_book"
    raise_exception = True

    def get_success_message(self, cleaned_data):
        message = 'Книгу {title} створено'
        return message.format(**cleaned_data)


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    form_class = BookForm
    success_url = reverse_lazy('books:books')
    permission_required = "books.change_book"
    raise_exception = True

    def get_success_message(self, cleaned_data):
        message = 'Книгу {title} відредаговано'
        return message.format(**cleaned_data)


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books:books')
    permission_required = "books.delete_product"
    raise_exception = True

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message({'title': self.object.title})

        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        message = 'Книгу {title} видалено'
        return message.format(**cleaned_data)
