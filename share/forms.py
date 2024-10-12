from django import forms
from .models import SharedRecipe, SharedRecipeComment

class SharedRecipeForm(forms.ModelForm):
    class Meta:
        model = SharedRecipe
        fields = ['title', 'image', 'ingredients', 'methods']

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        ingredients = cleaned_data.get('ingredients')
        methods = cleaned_data.get('methods')

        # Check if image is uploaded and its size
        if image:
            max_size = 10 * 1024 * 1024  # 10MB limit
            if image.size > max_size:
                self.add_error('image', 'The file size is too large. Maximum size is 10MB.')

        if not ingredients:
            self.add_error('ingredients', 'Ingredients are required.')

        if not methods:
            self.add_error('methods', 'Methods are required.')

        return cleaned_data

# Form to handle the comment data
class SharedRecipeCommentForm(forms.ModelForm):
    class Meta:
        model = SharedRecipeComment
        fields = ['body']
