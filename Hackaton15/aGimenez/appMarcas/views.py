from django.shortcuts import render
from rest_framework import generics
from .models import Marca
from .serializers import MarcaSerializer


# Create your views here.
class MarcaListCreateView(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class MarcaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer