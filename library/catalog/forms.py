from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Reader





class ReaderRegisterForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'middle_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control from-input', 'required': 'required',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
        }
