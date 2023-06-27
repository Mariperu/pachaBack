from django.db import models
from songs.models import Song


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
