
from django.contrib import admin
from .models import SharedRecipe, SharedRecipeComment  # Correct import

# Register SharedRecipe and SharedRecipeComment models with the admin site
admin.site.register(SharedRecipe)
admin.site.register(SharedRecipeComment)



