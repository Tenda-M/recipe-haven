from django import forms
from .models import SharedRecipe

class SharedRecipeForm(forms.ModelForm):
    class Meta:
        model = SharedRecipe
        fields = ['title', 'author', 'image', 'ingredients', 'methods']  # Include new fields
