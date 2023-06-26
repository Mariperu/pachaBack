from rest_framework import generics
from .models import Modelo
from .serializers import ModeloSerializer


class ModeloListCreateAPIView(generics.ListCreateAPIView):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer


class ModeloRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
