# Django
from django.urls import path

from users import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.profile),
    path('logout/', views.LogoutView.as_view(), name='logout')
]