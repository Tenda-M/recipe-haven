from django.urls import path
from . import views

urlpatterns = [
    # Use only one path for the share page that also displays shared recipes
    path('', views.share_page_view, name='share'),
]
