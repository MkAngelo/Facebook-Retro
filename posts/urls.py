"""URLs config."""

# Django
from django.urls import path

from posts import views


urlpatterns = [
    path('home/', views.home)
]