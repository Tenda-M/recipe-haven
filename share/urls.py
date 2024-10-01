from django.urls import path
from . import views

# this line to define the app name for namespacing
app_name = 'share'

urlpatterns = [
    path('', views.share_page_view, name='share'),
    path('edit/<int:recipe_id>/', views.edit_recipe_view, name='edit_recipe'),
    path('delete/<int:recipe_id>/', views.delete_recipe_view, name='delete_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe_detail_view, name='recipe_detail'),  
]
