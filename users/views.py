"""User views."""

# Django
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# Exception
from django.db.utils import IntegrityError

# Models
from users.models import Profile, User
from posts.models import Post

# Forms
from users.forms import SignupForm


class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/login.html'


def signup(request):
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/login.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/login.html', {'error': 'Username is already in use'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.sex = request.POST['gender']
        profile.save()

        return redirect('users:login')

    return render(request, 'users/login.html')


class UserDetailView(LoginRequiredMixin, DetailView):
    """User Detail View."""

    template_name = 'users/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = (
            Post.objects.filter(user=user).order_by('-timestamp')
        )
        return context


class SignUpView(FormView):
    
    template_name = 'users/login.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)