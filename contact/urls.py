from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),  # Contact Us page
    path('success/', views.contact_success, name='contact_success'),
    # Success page
]
