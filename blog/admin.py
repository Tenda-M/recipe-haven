from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')  # Added space after the comma
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register the Comment model
admin.site.register(Comment)
