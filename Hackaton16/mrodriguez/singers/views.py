from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serializers import SingerModelSerializer, SingerSerilaizer
from .models import Singer


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SingerModelSerializer
