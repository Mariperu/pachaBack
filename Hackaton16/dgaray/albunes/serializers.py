from rest_framework import serializers

from .models import Album

class AlbumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class AlbumSerilaizer(serializers.Serializer):
    # song = serializers.HiddenField(default = 'auto-user')
    # name = serializers.CharField(max_length=250)

    def create(self, data):
        album = Album.objects.create(**data)
        return album
