from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Choices for the status field in the Post model
STATUS = ((0, "Draft"), (1, "Published"))


# Post model representing blog posts in the application
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Post title
    slug = models.SlugField(max_length=200, unique=True)
    # URL slug for the post
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )  # The author of the post, linked to Django's User model

    # Cloudinary field for the featured image
    featured_image = CloudinaryField('image', default='placeholder')

    content = models.TextField()  # Main content of the post
    created_on = models.DateTimeField(auto_now_add=True)
    # Timestamp when the post is created
    updated_on = models.DateTimeField(auto_now=True)
    # Timestamp when the post is last updated
    status = models.IntegerField(choices=STATUS, default=0)
    # Status (Draft or Published)
    excerpt = models.TextField(blank=True)  # Optional excerpt for the post

    # Meta options for the Post model
    class Meta:
        ordering = ["-created_on"]  # Orders posts by most recent first

    # String representation of the Post model
    def __str__(self):
        return f"{self.title} | written by {self.author}"


# Comment model representing comments on blog posts
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )  # Each comment is linked to a specific post

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )  # Each comment has an author (user)

    body = models.TextField()  # The content of the comment
    approved = models.BooleanField(default=False)
    # Whether the comment is approved or not
    created_on = models.DateTimeField(auto_now_add=True)
    # Timestamp for when the comment was created

    # Meta options for the Comment model
    class Meta:
        ordering = ["created_on"]  # Orders comments by oldest first

    # String representation of the Comment model
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
