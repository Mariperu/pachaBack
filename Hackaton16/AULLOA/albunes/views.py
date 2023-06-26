from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Serializers
from .serializers import (AlbumModelSerializer, AlbumSerilaizer)

# Models
from .models import Album

# Create your views here.

class AlbumViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = AlbumModelSerializer

    def get_queryset(self):
        """Restrict list to only user Education."""
        queryset = Album.objects.all()
        return queryset

        
    def create(self, request, *args, **kwargs):
        serializer = AlbumSerilaizer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = AlbumModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()