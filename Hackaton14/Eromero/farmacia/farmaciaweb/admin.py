from django.contrib import admin
from .models import Usuario, Producto, Cliente, Compra

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Compra)
