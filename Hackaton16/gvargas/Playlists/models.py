from django.db import models

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=150, null=False, default='Playlist')

    def __str__(self):
        return self.name
