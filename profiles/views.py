from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from share.models import SharedRecipe  # Import the SharedRecipe model

# Credit: https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL
# -osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9


@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    # Get recipes shared by the user
    user_recipes = SharedRecipe.objects.filter(shared_by=request.user)

    return render(request, 'profiles/profile.html', {
        'profile': profile,
        'user_recipes': user_recipes
    })
