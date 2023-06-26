from django.urls import path
from .views import (
    MarcaListCreateView,
    MarcaRetrieveUpdateDestroyView,
    TipoListCreateView,
    TipoRetrieveUpdateDestroyView
)

urlpatterns = [
    path('marcas/', MarcaListCreateView.as_view(), name='marca-list'),
    path('marcas/<int:pk>/', MarcaRetrieveUpdateDestroyView.as_view(), name='marca-detail'),
    path('tipos/', TipoListCreateView.as_view(), name='tipo-list'),
    path('tipos/<int:pk>/', TipoRetrieveUpdateDestroyView.as_view(), name='tipo-detail'),
]
