from django.db import models
from albums.models import Album


class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    musical_genre = models.CharField(max_length=50)
    description = models.TextField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=500)

    def __str__(self):
        return self.name
