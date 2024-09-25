from django.contrib import admin
from .models import ContactUsForm
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(ContactUsForm)
class ContactUsFormAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('message', 'read',)

