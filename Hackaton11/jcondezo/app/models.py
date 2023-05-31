from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError
import datetime
from app import db

class Rol(db.Model):

    __tablename__ = 'model_rol'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<Rol {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1

    def public_url(self):
        return url_for('public.show_rol', slug=self.nombre)

    @staticmethod
    def get_all():
        return Rol.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Rol.query.get(id)


class Categoria(db.Model):

    __tablename__ = 'model_categoria'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Categoria {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1

    def public_url(self):
        return url_for('public.show_categoria', slug=self.nombre)

    @staticmethod
    def get_by_slug(slug):
        return Categoria.query.filter_by(nombre=slug).first()

    @staticmethod
    def get_all():
        return Categoria.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Categoria.query.get(id)


class Producto(db.Model):

    __tablename__ = 'model_producto'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    marca = db.Column(db.String, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('model_categoria.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1

    def public_url(self):
        return url_for('public.show_producto', slug=self.nombre)

    @staticmethod
    def get_by_slug(slug):
        return Producto.query.filter_by(nombre=slug).first()

    @staticmethod
    def get_all():
        return Producto.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Producto.query.get(id)

    @staticmethod
    def all_paginated(page=1, per_page=20):
        return Producto.query.order_by(Producto.created.asc()). \
            paginate(page=page, per_page=per_page, error_out=False)


class Cliente(db.Model):

    __tablename__ = 'model_cliente'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    dni = db.Column(db.String(12), nullable=False)
    celular = db.Column(db.String(9), nullable=True)
    direccion = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f'<Cliente {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1

    def public_url(self):
        return url_for('public.show_cliente', slug=self.nombre)

    @staticmethod
    def get_by_slug(slug):
        return Cliente.query.filter_by(nombre=slug).first()

    @staticmethod
    def get_all():
        return Cliente.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Cliente.query.get(id)

    @staticmethod
    def all_paginated(page=1, per_page=20):
        return Cliente.query.order_by(Cliente.created.asc()). \
            paginate(page=page, per_page=per_page, error_out=False)


class Factura(db.Model):

    __tablename__ = 'model_factura'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime(), default=datetime.datetime.utcnow, nullable=False)
    # cliente_id = db.Column(db.Integer, db.ForeignKey('model_cliente.id', ondelete='CASCADE'), nullable=False)
    # cliente = db.Column(db.String(256), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('model_cliente.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('model_user.id', ondelete='CASCADE'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('model_producto.id', ondelete='CASCADE'), nullable=False)
    # factura_id = db.Column(db.Integer, db.ForeignKey('model_factura.id', ondelete='CASCADE'), nullable=False)
    Cantidad = db.Column(db.Integer, nullable=False)
    MontoTotal = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Factura {self.fecha}>'

    def save(self):
        if not self.id:
            db.session.add(self)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1

    def public_url(self):
        return url_for('public.show_factura', slug=self.fecha)

    @staticmethod
    def get_by_slug(slug):
        return Factura.query.filter_by(fecha=slug).first()

    @staticmethod
    def get_all():
        return Factura.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Factura.query.get(id)

    @staticmethod
    def all_paginated(page=1, per_page=20):
        return Factura.query.order_by(Factura.created.asc()). \
            paginate(page=page, per_page=per_page, error_out=False)

