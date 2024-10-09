from django import forms
from .models import SharedRecipe, SharedRecipeComment

class SharedRecipeForm(forms.ModelForm):
    class Meta:
        model = SharedRecipe
        fields = ['title', 'author', 'image', 'ingredients', 'methods']  # Include new fields

    # Fix the indentation issue here
    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        ingredients = cleaned_data.get('ingredients')
        methods = cleaned_data.get('methods')

        if not image:
            self.add_error('image', 'Image is required.')
        if not ingredients:
            self.add_error('ingredients', 'Ingredients are required.')
        if not methods:
            self.add_error('methods', 'Methods are required.')

# Form to handle the comment data
class SharedRecipeCommentForm(forms.ModelForm):
    class Meta:
        model = SharedRecipeComment
        fields = ['body']
