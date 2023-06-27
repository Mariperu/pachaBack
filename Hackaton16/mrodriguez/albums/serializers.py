from rest_framework import serializers
from .models import Album


class AlbumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class AlbumSerializer(serializers.Serializer):
    def create(self, data):
        album = Album.objects.create(**data)
        return album
