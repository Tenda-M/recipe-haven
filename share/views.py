from django.shortcuts import render, get_object_or_404, redirect
from .models import SharedRecipe
from .forms import SharedRecipeForm 
from django.contrib.auth.decorators import login_required

@login_required
def edit_recipe_view(request, recipe_id):
    recipe = get_object_or_404(SharedRecipe, id=recipe_id, shared_by=request.user)

    if request.method == 'POST':
        form = SharedRecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile_view')  # Redirect to profile after saving
    else:
        form = SharedRecipeForm(instance=recipe)

    return render(request, 'share/edit_recipe.html', {'form': form})

@login_required
def delete_recipe_view(request, recipe_id):
    recipe = get_object_or_404(SharedRecipe, id=recipe_id, shared_by=request.user)
    
    if request.method == 'POST':
        recipe.delete()
        return redirect('profiles:profile_view')  # Redirect to profile after deleting

    return render(request, 'share/delete_recipe.html', {'recipe': recipe})

def share_page_view(request):
    # logic for the view
    shared_recipes = SharedRecipe.objects.all()
    return render(request, 'share/shared_recipes.html', {'shared_recipes': shared_recipes})

def recipe_detail_view(request, recipe_id):
    recipe = get_object_or_404(SharedRecipe, id=recipe_id)
    return render(request, 'share/recipe_detail.html', {'recipe': recipe})


