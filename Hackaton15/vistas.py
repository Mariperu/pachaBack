from rest_framework import generics
from .models import Marca, Tipo
from .serializers import MarcaSerializer, TipoSerializer

class MarcaListCreateView(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class MarcaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class TipoListCreateView(generics.ListCreateAPIView):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class TipoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
