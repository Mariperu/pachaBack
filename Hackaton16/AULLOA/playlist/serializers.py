from rest_framework import serializers

from .models import Playlist

class PlaylistModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class PlaylistSerilaizer(serializers.Serializer):
    # song = serializers.HiddenField(default = 'auto-user')
    # name = serializers.CharField(max_length=250)

    def create(self, data):
        album = Playlist.objects.create(**data)
        return album
