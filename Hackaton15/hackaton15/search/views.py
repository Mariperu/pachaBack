# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
# Permissions
from rest_framework.permissions import IsAuthenticated

# Models
from users.models import User

# Serializers
from search.serializers import TiendaSerializer

# Permissions
from users.permissions import IsRecruiterUser


class SearchViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True, is_recruiter=False)
    serializer_class = TiendaSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsRecruiterUser]
        return [permission() for permission in permission_classes]

class SearchViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    filter_backends = (SearchFilter,)
    queryset = User.objects.filter(is_active=True, is_recruiter=False)
    serializer_class = TiendaSerializer
    search_fields = (
            'first_name',
            'last_name',
            'email',
            'tipo',
            'marca',
            'auto',
    )