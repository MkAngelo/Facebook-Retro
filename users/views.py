from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/login.html'


def profile(request):
    return render(request, 'users/profile.html')