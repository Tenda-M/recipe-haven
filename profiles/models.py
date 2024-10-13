from django.db import models
from django.contrib.auth.models import User


# It extends the default User model to store additional user information.
class Profile(models.Model):
    # One-to-one relationship with the User model
    # When the related User is deleted, the Profile is also deleted
    # (on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Users can leave these fields blank (blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    # Image field for the profile picture
    # The image will be uploaded to the 'profile_pics/' directory
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # A text field for the user's biography or personal description
    # This field is optional (blank=True)
    bio = models.TextField(blank=True)

    # Add a blank line before the __str__ method to comply with PEP8
    def __str__(self):
        return f'{self.user.username} Profile'
