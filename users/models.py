from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):

    email = models.EmailField(
        _('email address'), 
        unique=True 
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, blank=True)
    friends = models.PositiveIntegerField(default=0)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    
    SEX_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    ]

    RELATION_CHOICES = [
        ('R', 'En una relación'),
        ('N', 'Solter@'),
        ('D', 'Es complicado'),
        ('V', 'Viud@'),
    ]

    sex = models.CharField(
        max_length=2,
        choices=SEX_CHOICES,
        default='H'
    )
    relation = models.CharField(
        max_length=2,
        choices=RELATION_CHOICES,
        default='N'
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return str(self.user)