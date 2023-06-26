from django.urls import path
from . import views

urlpatterns = [
    path('tipos', views.TipoListCreateAPIView.as_view(), name='tipo-list'),
    path('tipos/<int:pk>', views.TipoRetrieveUpdateDestroyAPIView.as_view(), name='tipo-detail'),
]
