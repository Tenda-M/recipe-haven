from django.shortcuts import render, get_object_or_404, redirect
from django.db import models  # Add this import to use models.Q for queries
from .models import SharedRecipe, SharedRecipeComment
from .forms import SharedRecipeCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SharedRecipeForm  # Add this line if it's missing


@login_required
def edit_recipe_view(request, recipe_id):
    recipe = get_object_or_404(
        SharedRecipe, id=recipe_id, shared_by=request.user
    )

    if request.method == 'POST':
        form = SharedRecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile_view')  # Redirect after saving
    else:
        form = SharedRecipeForm(instance=recipe)

    return render(request, 'share/edit_recipe.html', {'form': form})


@login_required
def delete_recipe_view(request, recipe_id):
    recipe = get_object_or_404(
        SharedRecipe, id=recipe_id, shared_by=request.user
    )

    if request.method == 'POST':
        recipe.delete()
        return redirect('profiles:profile_view')  # Redirect after deleting

    return render(request, 'share/delete_recipe.html', {'recipe': recipe})


@login_required
def share_page_view(request):
    shared_recipes = SharedRecipe.objects.all()

    if request.method == 'POST':
        form = SharedRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            shared_recipe = form.save(commit=False)
            shared_recipe.shared_by = request.user
            shared_recipe.save()
            messages.success(request, 'Recipe shared successfully!')
            return redirect('share:share')  # Redirect back to share page
        else:
            messages.error(
                request,
                'There was an error with your submission. Please try again.'
            )
    else:
        form = SharedRecipeForm()

    return render(
        request,
        'share/shared_recipes.html',
        {'shared_recipes': shared_recipes, 'form': form}
    )

@login_required
def recipe_detail_view(request, recipe_id):
    recipe = get_object_or_404(SharedRecipe, id=recipe_id)

    comments = recipe.comments.filter(
        models.Q(approved=True) | models.Q(author=request.user)
    ).order_by('-created_on')

    if request.method == 'POST':
        comment_form = SharedRecipeCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.success(request,
                             'Comment submitted and awaiting approval.')
            return redirect('share:recipe_detail', recipe_id=recipe.id)
    else:
        comment_form = SharedRecipeCommentForm()

    return render(
        request,
        'share/recipe_detail.html',
        {'recipe': recipe, 'comments': comments, 'comment_form': comment_form}
    )


@login_required
def edit_shared_recipe_comment(request, comment_id):
    comment = get_object_or_404(
        SharedRecipeComment, id=comment_id, author=request.user
    )

    if request.method == 'POST':
        form = SharedRecipeCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been updated.')
            return redirect('share:recipe_detail', recipe_id=comment.recipe.id)
    else:
        form = SharedRecipeCommentForm(instance=comment)

    return render(request, 'share/edit_comment.html', {'form': form})


@login_required
def delete_shared_recipe_comment(request, comment_id):
    comment = get_object_or_404(
        SharedRecipeComment, id=comment_id, author=request.user
    )

    if request.method == 'POST':
        recipe_id = comment.recipe.id
        comment.delete()
        messages.success(request, 'Your comment has been deleted.')
        return redirect('share:recipe_detail', recipe_id=recipe_id)

    return render(request, 'share/delete_comment.html', {'comment': comment})
