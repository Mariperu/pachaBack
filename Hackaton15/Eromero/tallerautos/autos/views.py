from rest_framework import viewsets
from .models import Marca, Tipo, Auto
from .serializers import MarcaSerializer, TipoSerializer, AutoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

    def get_queryset(self):
        """ Filtra los autos por marca y/o modelo si se proporcionan en los parámetros de consulta """
        queryset = super().get_queryset()
        marca = self.request.query_params.get('marca', None)  # type: ignore
        modelo = self.request.query_params.get('modelo', None)  # type: ignore
        if marca is not None:
            queryset = queryset.filter(marca__nombre=marca)
        if modelo is not None:
            queryset = queryset.filter(nombre=modelo)
        return queryset

