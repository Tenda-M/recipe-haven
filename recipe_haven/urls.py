"""
URL configuration for recipe_haven project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# For serving media files (e.g., profile images)
from django.conf import settings
from django.conf.urls.static import static

# Defining URL patterns for various apps in the project
urlpatterns = [
    # Profile URLs - to manage user profiles
    path('profile/', include('profiles.urls', namespace='profiles')),

    # Share URLs - to handle recipe sharing
    path('share/', include(('share.urls', 'share'), namespace='share')),

    # Contact page URLs - for contact form and handling contact-related views
    path("contact/", include("contact.urls")),

    # About page URLs - static pages about the website
    path("about/", include("about.urls"), name="about-urls"),

    # FAQ page URLs - for frequently asked questions
    path('faq/', include('faq.urls')),

    #User authentication URLs (allauth package) - handles login,
    #registration, etc."""
    path("accounts/", include("allauth.urls")),

    # Admin URLs - for the Django admin interface
    path('admin/', admin.site.urls),

    # Summernote URLs - for rich text editor functionality in admin and forms
    path('summernote/', include('django_summernote.urls')),

    # Blog URLs - main content for the site, such as blog posts and recipes
    path("", include("blog.urls"), name="blog-urls"),
]

# Serving media files during development (e.g., profile images, recipe images)
# In production, media files should be served by the web server (e.g., Nginx)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
