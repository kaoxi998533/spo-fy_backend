from django.contrib import admin
from .models import Album, Song, Video, Comment, Like

class AlbumAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'artist_name', 'cover_url')
    # search_fields = ('name', 'artist_name')
    None

class SongAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'artist_name', 'duration', 'album')
    # search_fields = ('name', 'artist_name')
    # list_filter = ('album',)
    None

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'song', 'user', 'title', 'duration', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'video', 'user', 'content', 'created_at')
    search_fields = ('user__username', 'video__title', 'content')
    list_filter = ('created_at',)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'video', 'user', 'created_at')
    search_fields = ('user__username', 'video__title')
    list_filter = ('created_at',)

admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
