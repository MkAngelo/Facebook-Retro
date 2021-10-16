from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import views as auth_views


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

def profile(request):
    return render(request, 'users/profile.html')