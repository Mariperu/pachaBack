from django.db import models
from artistas.models import Artist
from playlist.models import Playlist
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250, null=False, default='')
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=300, null=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.DO_NOTHING, null=True, default='')
    playlist_id = models.ForeignKey(Playlist, on_delete=models.DO_NOTHING, null=True, default='')

    def __str__(self):
        return self.name