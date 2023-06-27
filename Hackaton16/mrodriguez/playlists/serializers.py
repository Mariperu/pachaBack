from rest_framework import serializers
from .models import Playlist


class PlaylistModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"


class PlaylistSerilaizer(serializers.Serializer):
    def create(self, data):
        playlist = Playlist.objects.create(**data)
        return playlist
