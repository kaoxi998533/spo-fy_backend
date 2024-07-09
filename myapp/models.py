import allauth.models
import allauth.socialaccount
import allauth.socialaccount.models
from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    cover_url = models.TextField()

    def __str__(self):
        return self.name

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=255)
    duration = models.IntegerField()
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
class Video(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_path = models.FileField(upload_to='videos')
    duration = models.IntegerField()
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    video = models.ForeignKey(Video, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'comment by {self.user.username}'

class Like(models.Model):
    video = models.ForeignKey(Video, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('video', 'user')

    def __str__(self):
        return f'{self.user.username} likes {self.video.title}'