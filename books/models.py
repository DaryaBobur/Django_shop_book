from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Назва: {self.title}. Автор: {self.author}. Ціна: {self.price}. Опис: {self.description} Кількість на складі: {self.stock}"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']


