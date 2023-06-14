from django.urls import path
from . import views

app_name = 'checking'
urlpatterns = [
    path('vuelo/', views.ListVuelosView.as_view(), name='index'),
    path('vuelo/add/', views.AddVueloView.as_view(), name='view'),
    path('vuelo/<pk>/', views.DetailVuelosView.as_view(), name='detail'),
    path('vuelo/<pk>/delete', views.DeleteVuelosView.as_view(), name='delete'),
    path('vuelo/<pk>/update', views.UpdateVuelosView.as_view(), name='update'),
    path('tipoasiento/', views.ListTipoAsientoView.as_view(), name='view'),
    path('tipoasiento/add', views.AddTipoAsientoView.as_view(), name='view'),
    path('tipoasiento/<pk>/', views.DeleteTipoAsientoView.as_view(), name='detail'),
    path('tipoasiento/<pk>/delete', views.DeleteTipoAsientoView.as_view(), name='delete'),
    path('tipoasiento/<pk>/update', views.UpdateTipoAsientoView.as_view(), name='update'),
]