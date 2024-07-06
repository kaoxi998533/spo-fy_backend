from django.db import models

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

