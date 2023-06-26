from django.db import models
from django.contrib.auth.models import User

class Artista(models.Model):
    nombre = models.CharField(max_length=100)

class Album(models.Model):
    nombre = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='albums')

class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='canciones')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canciones')

class Playlist(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    canciones = models.ManyToManyField(Cancion, related_name='playlists')
