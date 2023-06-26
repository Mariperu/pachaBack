from django.urls import path
from . import views

urlpatterns = [
    path('modelos', views.ModeloListCreateAPIView.as_view(), name='modelo-list'),
    path('modelos/<int:pk>', views.ModeloRetrieveUpdateDestroyAPIView.as_view(), name='modelo-detail'),
]
