from django import forms
from .models import Book


class BookCreationModelForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = (
            'name',
            'author',
            'cover',
            'category'
        )