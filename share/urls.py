from django.urls import path
from . import views

app_name = 'share'

urlpatterns = [
    path('', views.share_page_view, name='share'),
    path('recipe/<int:recipe_id>/', views.recipe_detail_view, name='recipe_detail'),  # URL pattern for detailed view
]
