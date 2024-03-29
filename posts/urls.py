"""URLs config."""

# Django
from django.urls import path

from posts import views


urlpatterns = [
    path('', views.list_posts, name='home'),
    path('create/', views.create_post, name='create'),
]