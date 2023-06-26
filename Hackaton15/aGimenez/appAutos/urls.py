from django.urls import path
from . import views

urlpatterns = [
    path('autos', views.AutoListCreateAPIView.as_view(), name='auto-list'),
    path('autos/<int:pk>', views.AutoRetrieveUpdateDestroyAPIView.as_view(), name='auto-detail'),
]