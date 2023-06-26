from django.db import models
from Canciones.models import Song
# Create youmodels here.
class Album(models.Model):
    name = models.CharField(max_length=150, null=False, default='albunes')
    song_id = models.ForeignKey(Song, on_delete=models.DO_NOTHING, null=True, default='')

    def __str__(self):
        return self.name
