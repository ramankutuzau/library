from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Reader





# class ReaderRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Reader
#         fields = ['first_name', 'last_name', ]
#
# class ReturnBookForm(forms.Form):
#     book_code = forms.CharField(label='Код книги')
