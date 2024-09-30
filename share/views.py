from django.shortcuts import render, redirect
from .forms import SharedRecipeForm
from .models import SharedRecipe

def share_page_view(request):
    if request.method == 'POST':
        form = SharedRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            shared_recipe = form.save(commit=False)
            shared_recipe.shared_by = request.user
            shared_recipe.save()
            return redirect('share')  # Redirect to refresh the page after submission
    else:
        form = SharedRecipeForm()

    shared_recipes = SharedRecipe.objects.all()
    return render(request, 'share/shared_recipes.html', {'form': form, 'shared_recipes': shared_recipes})
