from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AlbumModelSerializer, AlbumSerializer
from .models import Album


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlbumModelSerializer


@api_view(["DELETE"])
def AlbumDeleteView(req, id):
    album = get_object_or_404(Album, id=id)
    album.delete()
    return Response({"message": "Eliminado correctamente."})
