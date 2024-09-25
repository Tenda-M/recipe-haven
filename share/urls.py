from django.urls import path
from . import views

urlpatterns = [
    path('', views.share_view, name='share'),
    path('shared_books/', views.shared_books_view, name='shared_books'),
]
