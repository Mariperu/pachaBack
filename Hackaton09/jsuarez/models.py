from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):

    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)


users = []


def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None


class Alumnos:
    def __init__(self, id, nombre, identificador, edad, correo):
        self.id = id
        self.nombre = nombre
        self.identificador = identificador
        self.edad = edad
        self.correo = correo
    
    def __repr__(self):
        return '<Alumno {}>'.format(self.nombre)

class Profesores:
    def __init__(self, id, nombre, identificador, edad, correo):
        self.id = id
        self.nombre = nombre
        self.identificador = identificador
        self.edad = edad
        self.correo = correo
    
    def __repr__(self):
        return '<Profesor {}>'.format(self.nombre)

class Cursos:
    def __init__(self, id, nombre, identificador):
        self.id = id
        self.nombre = nombre
        self.identificador = identificador
    
    def __repr__(self):
        return '<Curso {}>'.format(self.nombre)

class Salones:
    def __init__(self, id, nombre, anioEscolar):
        self.id = id
        self.nombre = nombre
        self.anioEscolar = anioEscolar
    
    def __repr__(self):
        return '<Salon {}>'.format(self.nombre)