from django.contrib import admin
from .models import Pasajero, Compra, TipoAsiento, Asiento, Avion, Vuelo, BoardingPass
# Register your models here.

admin.site.register(Pasajero)
admin.site.register(Compra)
admin.site.register(TipoAsiento)
admin.site.register(Asiento)
admin.site.register(Avion)
admin.site.register(Vuelo)
admin.site.register(BoardingPass)
