from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serializers import UserModelSerializer, UserSerilaizer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserModelSerializer
