# Django
from django.urls import path

from users import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/<str:username>/', views.UserDetailView.as_view(), name='detail'),
    path('me/update/', views.UpdateProfile.as_view(), name='update_profile'),
]