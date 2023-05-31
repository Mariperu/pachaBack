from orator import Model, DatabaseManager, SoftDeletes
from orator.orm import belongs_to, has_many
from flask_login import UserMixin
from config import db

Model.set_connection_resolver(db)

class Usuario(UserMixin, Model):
    __table__ = 'usuarios'
    __fillable__ = ['nombre', 'correo', 'password', 'rol']

class Producto(Model):
    __table__ = 'productos'
    __fillable__ = ['nombre', 'categoria', 'stock', 'precio']

class Factura(Model):
    __table__ = 'facturas'
    __fillable__ = ['usuario_id', 'producto_id', 'cantidad', 'total']

    @belongs_to('usuario_id')
    def usuario(self):
        return Usuario

    @belongs_to('producto_id')
    def producto(self):
        return Producto

class Comprador(Usuario):
    __table__ = 'compradores'
    __fillable__ = ['nombre', 'correo']

    @has_many('usuario_id', 'id')
    def compras(self):
        return Factura

