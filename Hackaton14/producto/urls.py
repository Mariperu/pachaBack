from django.urls import path
from . import views

app_name = 'producto'
urlpatterns = [
    path('prod/', views.ListProductoView.as_view(), name='index'),
    path('prod/add/', views.AddProducto.as_view(), name='view'),
    path('prod/<pk>/update', views.UpdateProductos.as_view(), name='update'),
    path('prod/<pk>/delete', views.DeleteProductos.as_view(), name='delete'),

    path('boleta/', views.ListBoleta.as_view(), name='view_boleta'),
    path('boleta/add/', views.registrar_boleta, name='addBoleta'),

    path('cliente/', views.ListClienteView.as_view(), name='view_cliente'),
]