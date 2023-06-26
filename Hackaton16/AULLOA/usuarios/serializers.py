from rest_framework import serializers

from .models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerilaizer(serializers.Serializer):
    # song = serializers.HiddenField(default = 'auto-user')
    # name = serializers.CharField(max_length=250)

    def create(self, data):
        album = User.objects.create(**data)
        return album
