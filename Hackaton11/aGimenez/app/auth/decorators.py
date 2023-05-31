from functools import wraps
from flask import abort
from flask_login import current_user


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):

        is_admin = getattr(current_user, 'rol', 'administrador')
        if not is_admin:
            abort(401)
        return f(*args, **kws)
    return decorated_function

def almacen_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_almacen = getattr(current_user, 'rol', 'almacen')
        if not is_almacen:
            abort(401)
        return f(*args, **kws)
    return decorated_function

def cajero_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_cajero = getattr(current_user, 'rol', 'cajero')
        if not is_cajero:
            abort(401)
        return f(*args, **kws)
    return decorated_function

def client_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_client = getattr(current_user, 'rol', 'cliente')
        if not is_client:
            abort(401)
        return f(*args, **kws)
    return decorated_function