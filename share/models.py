from django.db import models  # Import models from django.db
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class SharedRecipe(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    image = CloudinaryField('image', blank=False, null=False)  # Image is required
    ingredients = models.TextField(default="No ingredients provided", blank=False, null=False)  # Required
    methods = models.TextField(default="No methods provided", blank=False, null=False)  # Required
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def ingredients_excerpt(self):
        return self.ingredients[:100]  # Show the first 100 characters of ingredients

    @property
    def methods_excerpt(self):
        return self.methods[:100]  # Show the first 100 characters of methods


# To Ensure the code has a comment model linked to SharedRecipe
class SharedRecipeComment(models.Model):
    recipe = models.ForeignKey(SharedRecipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author} on {self.recipe}'
