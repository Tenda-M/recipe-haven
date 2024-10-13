from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Custom admin class for the About model.
    """
    summernote_fields = ('content',)

# Newline at the end of the file
