from flask import Blueprint

factura_bp = Blueprint('factura', __name__, template_folder='templates')
# producto_bp = Blueprint('producto', __name__, template_folder='templates')

from . import routes