from django.db import models
from users.models import User, Profile

# Create your models here.
class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='posts/photos', blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.content} by @ {self.user.username}'

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    
    @property
    def get_like_count(self):
        return self.like_set.all().count()


class Comment(models.Model):
    """User comments"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username
    

class Like(models.Model):
    """Post Like."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username