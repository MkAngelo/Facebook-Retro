from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView,CreateView
from django.urls.base import reverse_lazy

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


@login_required
def list_posts(request):
    """List existing posts."""
    posts = Post.objects.all().order_by('-timestamp')

    return render(request, 'posts/home.html', {'posts': posts})


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:home')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
