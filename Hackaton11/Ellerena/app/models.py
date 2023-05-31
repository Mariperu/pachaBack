from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(256), nullable=False)
    precio = db.Column(db.String(256), nullable=False)
    stock = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<Post {self.producto} {self.precio} {self.stock}>'

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

    @staticmethod
    def get_by_id(slug):
        return Product.query.filter_by(id=id).first()
