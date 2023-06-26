from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login_app, name="login"),
    path("register/", views.register, name="register"),

    path("admin_farmacia/", views.is_admin, name='admin_farmacia'),
    path("seller/", views.is_seller, name='seller'),

    path('api/venta/<str:id_cliente>/<str:id_producto>', views.reggister_sale , name='ventas'),
    path('api/reporte/<str:id_producto>', views.getReporte , name='reporte')
]
