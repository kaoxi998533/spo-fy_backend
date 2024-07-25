from django.contrib import admin
from .models import Profile, Follower

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'portrait')

class FollowerAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to', 'created')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follower, FollowerAdmin)
