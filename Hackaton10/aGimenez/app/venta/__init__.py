from flask import Blueprint

venta_bp = Blueprint('venta', __name__, template_folder='templates')

from . import routes