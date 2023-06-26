
# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandardUser

# Models
from marca.models import Marca

#Serializers
from marca.serializers import (MarcaModelSerializer, MarcaSerializer)


class MarcaViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin, viewsets.GenericViewSet):

    serializer_class = MarcaModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]


    def create(self, request, *args, **kwargs):
        serializer = MarcaSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = MarcaModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = Marca.objects.filter(user=self.request.user)
        return queryset
