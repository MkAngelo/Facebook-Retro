"""User's admin dash."""

# Django
from django.contrib import admin

# Models
from users.models import Profile, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin."""

    list_display = ('email', 'first_name', 'last_name')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('user', 'status', 'friends', 'picture', 'sex', 'relation')