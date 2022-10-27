from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    
class Song(models.Model):
    title = models.CharField(max_length=50)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    release_date = models.DateField()
class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    
