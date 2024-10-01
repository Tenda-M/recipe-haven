from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile_view(request):
    try:
        # Get the profile associated with the logged-in user
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # If the profile doesn't exist, create a new one
        profile = Profile.objects.create(user=request.user)
    
    # Debugging: Print profile image to console
    print(f"Profile Image: {profile.image}")
    
    # Render the profile.html template and pass the profile context
    return render(request, 'profiles/profile.html', {'profile': profile})
