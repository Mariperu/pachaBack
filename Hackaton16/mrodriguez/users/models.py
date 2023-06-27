from django.db import models
from singers.models import Singer
from playlists.models import Playlist


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=False, default="")
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=300, null=True)
    artist = models.ForeignKey(
        Singer, on_delete=models.DO_NOTHING, null=True, default=""
    )
    playlist = models.ForeignKey(
        Playlist, on_delete=models.DO_NOTHING, null=True, default=""
    )

    def __str__(self):
        return self.name
