from rest_framework import generics
from .models import Auto
from .serializers import AutoSerializer


class AutoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AutoSerializer

    def get_queryset(self):
        print(self.request.query_params)
        if self.request.query_params:
            queryset = Auto.objects.filter(modelo__nombre=self.request.query_params.get("modelo"),
                                           modelo__marca__nombre=self.request.query_params.get("marca"))
        else:
            queryset = Auto.objects.all()
        return queryset


class AutoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
