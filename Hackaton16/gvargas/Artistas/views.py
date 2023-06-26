from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Serializers
from .serializers import (ArtistModelSerializer, ArtistSerilaizer)

# Models
from .models import Artist

# Create your views here.

class ArtistViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = ArtistModelSerializer

    def get_queryset(self):
        """Restrict list to only user Education."""
        queryset = Artist.objects.all()
        return queryset

        
    def create(self, request, *args, **kwargs):
        serializer = ArtistSerilaizer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = ArtistModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
