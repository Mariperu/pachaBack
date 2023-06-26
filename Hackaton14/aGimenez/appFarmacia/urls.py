from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='appFarmacia/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='appFarmacia/index.html'), name='logout'),

    path('producto/', views.ListProductosView.as_view(), name='list'),
    path('producto/add/', views.AddProductoView.as_view(), name='view'),
    path('producto/<pk>/', views.DetailProductosView.as_view(), name='detail'),
    path('producto/<pk>/delete', views.DeleteProductosView.as_view(), name='delete'),
    path('producto/<pk>/update', views.UpdateProductosView.as_view(), name='update'),

    path('facturas/', views.FacturaListView.as_view(), name='factura_list'),
    path('factura/', views.cargar_factura, name='cargar_factura'),
    path('factura/<pk>/', views.DetailFacturasView.as_view(), name='detailFactura'),
    path('factura/<int:pk>/exportar-txt/', ExportarFacturaTXTView.as_view(), name='exportar_factura_txt'),

    path('buscar_producto/', views.buscar_producto, name='buscar_producto'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)