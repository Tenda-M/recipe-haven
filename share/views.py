from django.shortcuts import render, get_object_or_404, redirect
from .models import SharedRecipe
from .forms import SharedRecipeForm 

def share_page_view(request):
    # If the request is POST, handle form submission
    if request.method == 'POST':
        form = SharedRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            shared_recipe = form.save(commit=False)
            shared_recipe.shared_by = request.user
            shared_recipe.save()
            return redirect('share:share')  # Redirect to the share page after submission
    else:
        form = SharedRecipeForm()

    # Query all shared recipes to display them on the same page
    shared_recipes = SharedRecipe.objects.all()

    # Render the form and shared recipes on the same page
    return render(request, 'share/shared_recipes.html', {'form': form, 'shared_recipes': shared_recipes})

def recipe_detail_view(request, recipe_id):
    # Retrieve the detailed recipe by ID
    recipe = get_object_or_404(SharedRecipe, id=recipe_id)
    return render(request, 'share/recipe_detail.html', {'recipe': recipe})
