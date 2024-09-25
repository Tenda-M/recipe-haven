from django import forms
from .models import SharedBook

class SharedBookForm(forms.ModelForm):
    class Meta:
        model = SharedBook
        fields = ['title', 'author', 'image']
