from django.contrib import admin
from .models import Rol,Producto,Usuario,FarmaciaUser,Pedido
# Register your models here.
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(FarmaciaUser)
admin.site.register(Pedido)