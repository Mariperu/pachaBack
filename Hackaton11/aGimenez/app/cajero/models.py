from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError
import datetime
from app import db

class Factura(db.Model):
    __tablename__ = 'factura'

    id = db.Column(db.Integer, primary_key=True)
    numero_factura = db.Column(db.String(50), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    cliente = db.Column(db.String(100), nullable=False)

    detalles = db.relationship('DetalleFactura', backref='factura', cascade='all, delete-orphan')
    def __repr__(self):
        return f'<Factura {self.numero_factura} {self.created} {self.cliente} {self.detalles}>'

    @property
    def total (self):
         return sum(detalle.subtotal for detalle in self.detalles)
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
                self.id = f'{self.id}-{count}'


    @staticmethod
    def get_by_slug(slug):
        return Factura.query.filter_by(numero_factura=slug).first()

    @staticmethod
    def get_by_cliente(slug):
        return Factura.query.filter_by(cliente=slug)
    @staticmethod
    def get_all():
        return Factura.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_numero_factura(numero_factura):
        return Factura.query.get(numero_factura)

    @staticmethod
    def all_paginated(page=1, per_page=10):
        return Factura.query.order_by(Factura.created.asc()). \
            paginate(page=page, per_page=per_page, error_out=False)

class DetalleFactura(db.Model):
    __tablename__ = 'detallefactura'

    id = db.Column(db.Integer, primary_key=True)
    factura_id = db.Column(db.Integer, db.ForeignKey('factura.id'),nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    cantProducto = db.Column(db.Integer)

    @property
    def subtotal(self):
        return self.cantProducto * self.precio

    def __repr__(self):
        return f'<DetalleFactura {self.nombre} {self.stock} {self.precio} {self.factura_id} {self.cantProducto} {self.subtotal}>'

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
                self.id = f'{self.id}-{count}'


    @staticmethod
    def get_by_slug(slug):
        return DetalleFactura.query.filter_by(nombre=slug).first()

    @staticmethod
    def get_all():
        return DetalleFactura.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return DetalleFactura.query.get(id)

    @staticmethod
    def all_paginated(page=1, per_page=10):
        return DetalleFactura.query.order_by(DetalleFactura.created.asc()). \
            paginate(page=page, per_page=per_page, error_out=False)
