from django.urls import path
from . import views

urlpatterns = [
    path('marcas', views.MarcaListCreateView.as_view(), name='marca-list'),
    path('marcas/<int:pk>', views.MarcaRetrieveUpdateDestroyView.as_view(), name='marca-detail'),
]