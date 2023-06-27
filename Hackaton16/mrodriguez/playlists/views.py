from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import PlaylistModelSerializer, PlaylistSerilaizer
from .models import Playlist


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlaylistModelSerializer
