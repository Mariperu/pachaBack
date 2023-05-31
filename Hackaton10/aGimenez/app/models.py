from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db 

class Product(db.Model):
    __tablename__ = "model_product"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(25), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precioUnitario = db.Column(db.Float, nullable=False)

  # Datos necesarios:
    def __init__(self, nombre, categoria, stock, precioUnitario):
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.precioUnitario = precioUnitario

    # Representación
    def __repr__(self):
        return f"<Product {self.nombre} {self.categoria} {self.stock} {self.precioUnitario}>"

    # add product
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

    # Métodos:
    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)

    # @staticmethod
    # def query_all(id):
    #     return Product.query.all(id)

class Venta(db.Model):
    __tablename__ = "model_venta"

    id = db.Column(db.Integer, primary_key=True)
    fechaVenta = db.Column(db.Date())
    nombre = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(25), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precioUnitario = db.Column(db.Float, nullable=False)
    subTotal = db.Column(db.Float, nullable=False)

  # Datos necesarios:
    def __init__(self, fechaVenta, nombre, categoria, stock, precioUnitario, subTotal):
        self.fechaVenta = fechaVenta
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.precioUnitario = precioUnitario
        self.subTotal = subTotal
    # Representación
    def __repr__(self):
        return f"<Product {self.fechaVenta} {self.nombre} {self.categoria} {self.stock} {self.precioUnitario} {self.subTotal}>"

    # add product
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

    # Métodos:
    @staticmethod
    def get_by_id(id):
        return Venta.query.get(id)

    # @staticmethod
    # def query_all(id):
    #     return Product.query.all(id)
