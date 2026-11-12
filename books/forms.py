from django import forms

from books.models import Category, Book


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        label="Категорія",
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву'
        })
    )

    class Meta:
        model = Category
        fields = ('name',)


class BookForm(forms.ModelForm):
    title = forms.CharField(
        label="Книги", max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву'
        })
    )
    description = forms.CharField(
        label="Опис товару", max_length=None,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть опис'
        })
    )
    price = forms.DecimalField(
        label="Ціна", widget=forms.NumberInput(
            attrs={'class': 'form-control', })
    )
    category = forms.ModelChoiceField(
        label='Категорія', queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control basic-single',  })
    )

    class Meta:
        model = Book
        fields = '__all__'