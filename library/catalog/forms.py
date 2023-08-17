from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelChoiceField

from .models import Reader, Book, Author


class MySelect:
    pass


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(), empty_label="Выберите автора", label='Автор',
        widget=forms.Select(attrs={
            'class': 'form-control',
        }), required=True,
    )

    class Meta:
        model = Book
        fields = ['code', 'title', 'author']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control from-input', 'required': 'required',}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
        }

class ReaderRegisterForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'middle_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
        }
