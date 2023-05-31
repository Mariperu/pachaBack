from flask_orator import Orator
from orator.orm import belongs_to, has_many

db = Orator()

class Cliente_table(db.Model):
    __table__ = 'cliente_tables'
    __primary_key__ = 'id_cliente'
    __timestamps__ = False
    __fillable__ = ['nombre', 'direccion', 'telefono']

class Producto_table(db.Model):
    __table__ = 'producto_tables'
    __primary_key__ = 'id_producto'
    __timestamps__ = False
    __fillable__ = ['nombre', 'precio', 'stock']

class Venta_table(db.Model):
    __table__ = 'venta_tables'
    __primary_key__ = 'id_venta'
    __timestamps__ = False
    __fillable__ = ['fecha_venta', 'monto_total', 'id_cliente']

    @belongs_to('id_cliente', 'id_cliente')
    def cliente(self):
        return Cliente_table

    @has_many('id_venta', 'id_venta')
    def detalle_ventas(self):
        return DetalleVenta_table

class DetalleVenta_table(db.Model):
    __table__ = 'detalle_venta_tables'
    __primary_key__ = 'id_detalle'
    __timestamps__ = False
    __fillable__ = ['cantidad', 'subtotal', 'id_producto', 'id_venta']
    
    @belongs_to('id_venta', 'id_venta')
    def venta(self):
        return Venta_table

    @belongs_to('id_producto', 'id_producto')
    def producto(self):
        return Producto_table
