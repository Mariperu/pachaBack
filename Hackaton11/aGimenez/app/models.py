from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError
import datetime
from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Product {self.nombre} {self.stock} {self.precio} {self.created}>'

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
                self.nombre = f'{self.nombre}-{count}'

    def public_url(self):
        return url_for('public.show_product', slug=self.nombre)

    @staticmethod
    def get_by_slug(slug):
        return Product.query.filter_by(nombre=slug).first()

    @staticmethod
    def get_all():
        return Product.query.all()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)

    @staticmethod
    def all_paginated(page=1, per_page=10):
        return Product.query.order_by(Product.created.asc()). \
            paginate(page=page, per_page=per_page, error_out=False)
