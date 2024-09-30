from django.db import models
from django.contrib.auth.models import User

class SharedRecipe(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipes/')
    ingredients = models.TextField(default="No ingredients provided")  # Default value
    methods = models.TextField(default="No methods provided")  # Default value
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
