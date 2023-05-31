from flask import Blueprint

almacen_bp = Blueprint('almacen', __name__, template_folder='templates')

from . import routes
