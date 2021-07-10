from django import forms
from django.forms import ModelForm
from .models import *

class addbookform(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            '__all__': forms.TextInput(attrs={'placeholder': 'Add new book...'}),
        }