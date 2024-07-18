from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    bio = models.TextField(null=True, blank=True)
    image_file = models.URLField()
    location = models.TextField(null=True, blank=True)
    name = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    cover_url = models.TextField()

    def __str__(self):
        return self.name

class AlbumInfo(models.Model):
    album = models.OneToOneField(Album, primary_key=True, on_delete=models.CASCADE)
    date_released = models.DateField(default='1970-01-01')
    type = models.TextField(default='Unknown Type', max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=255)
    duration = models.IntegerField()
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    date_recorded = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.TextField(max_length=40)

class SongInfo(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE, primary_key=True)
    genres = models.ManyToManyField(Genre, blank=True)
    instrumental = models.BooleanField()
    language = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return 'information of ' + self.song.name
    

class SongMetadata(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE)
    acousticness = models.FloatField()
    danceability = models.FloatField()
    energy = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    speechiness = models.FloatField()
    tempo = models.FloatField()
    valence = models.FloatField()
    hotness = models.FloatField()

    def __str__(self) -> str:
        return  'metadata of ' + self.song.name
    
    
    
class ArtistMetadata(models.Model):
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE)
    discovery_index = models.FloatField()
    familiarity_index = models.FloatField()
    hotness = models.FloatField()
    tags = models.ManyToManyField(Tag, related_name='artists')

    def __str__(self) -> str:
        return f'metadata for artist named {self.artist.name}'

class Listen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    listened_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        username = Profile.objects.get(id=self.user).username
        if not username:
            username = 'nameless user'
        return f'{username} listened to {self.song.name} at {str(self.listened_at)}'
    

class Video(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_path = models.FileField(upload_to='videos')
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        username = Profile.objects.get(id=self.user).username
        return f'video for {self.song} uploaded by {username} at {str(self.created_at)} titled {self.title}'

class Comment(models.Model):
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'comment by {self.user.username} in video of id {self.video}'

class Like(models.Model):
    video = models.ForeignKey(Video, related_name='video_likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('video', 'user')

    def __str__(self):
        return f'{self.user.username} likes {self.video.title}'
