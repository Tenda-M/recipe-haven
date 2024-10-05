from django import forms
from .models import SharedRecipe
from .models import SharedRecipeComment

class SharedRecipeForm(forms.ModelForm):
    class Meta:
        model = SharedRecipe
        fields = ['title', 'author', 'image', 'ingredients', 'methods']  # Include new fields

#form to handle the comment data.
class SharedRecipeCommentForm(forms.ModelForm):
    class Meta:
        model = SharedRecipeComment
        fields = ['body']
