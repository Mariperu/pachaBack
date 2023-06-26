from rest_framework import serializers

from .models import Artist

class ArtistModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ArtistSerilaizer(serializers.Serializer):
    # song = serializers.HiddenField(default = 'auto-user')
    # name = serializers.CharField(max_length=250)

    def create(self, data):
        album = Artist.objects.create(**data)
        return album
