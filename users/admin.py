"""User's admin dash."""

# Django
from django.contrib import admin

# Models
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('user', 'status', 'friends', 'picture', 'sex', 'relation')