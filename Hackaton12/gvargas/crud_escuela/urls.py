from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detalle_curso/<str:id>/', views.detalle_curso, name='detalle_curso'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('actualizar_curso/<str:id>/', views.actualizar_curso, name='actualizar_curso'),
    path('eliminar_curso/<str:id>/', views.eliminar_curso, name='eliminar_curso'),

]
