from django.contrib import admin
from .models import Album, Song, Video, Comment, Like

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_id', 'name', 'artist_name', 'cover_url')
    search_fields = ('name', 'artist_name')

class SongAdmin(admin.ModelAdmin):
    list_display = ('song_id', 'name', 'artist_name', 'duration', 'album')
    search_fields = ('name', 'artist_name')
    list_filter = ('album',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'song', 'user', 'title', 'duration', 'likes', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at',)
    readonly_fields = ('likes',)

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
