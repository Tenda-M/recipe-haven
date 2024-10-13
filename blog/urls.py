from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('comment/edit/<int:comment_id>/',
         views.edit_comment_view, name='edit_comment'),
    path('comment/delete/<int:comment_id>/',
         views.delete_comment_view, name='delete_comment'),
]
