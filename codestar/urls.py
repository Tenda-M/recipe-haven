"""
URL configuration for codestar project.

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

#For media profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', include('profiles.urls', namespace='profiles')),
    path('share/', include(('share.urls', 'share'), namespace='share')), 
    path("contact/", include("contact.urls")),  # Include the contact app's URLs
    path("about/", include("about.urls"), name="about-urls"),
    path('faq/', include('faq.urls')), 
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog-urls"),
    
]

# Profilen to serve media profile files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


