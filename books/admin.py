from django.contrib import admin

from .models import Book, Category

class BookInline(admin.TabularInline):
    model = Book
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category', 'stock')
    search_fields = ('author', 'category__name', 'title')
    list_filter = ('author', 'category__name')