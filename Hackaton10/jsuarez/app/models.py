from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db


class Perfil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('model_user.id', ondelete='CASCADE'), nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    apellido = db.Column(db.String(256), nullable=False)
    pais = db.Column(db.String(256), nullable=False)
    ciudad = db.Column(db.String(256), nullable=False)
    fechaNacimiento = db.Column(db.Date() , nullable=True)
    info = db.Column(db.Text)
    avatar = db.Column(db.String(256), nullable=True)
    url = db.Column(db.String(256), nullable=True)
    facebook = db.Column(db.String(256), nullable=True)
    twitter = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return f'<Post {self.nombre} {self.apellido}>'

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
        return Perfil.query.filter_by(id=id).first()
    

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
