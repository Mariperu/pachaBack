from django.db import models
from albunes.models import Album
# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    description = models.TextField()
    album_id = models.ForeignKey(Album, on_delete=models.DO_NOTHING, null=True, default='')
    img_path = models.CharField(max_length=500, null=True, default='')

    def __str__(self):
        return self.nombre