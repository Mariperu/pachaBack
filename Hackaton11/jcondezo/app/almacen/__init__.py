from flask import Blueprint

categoria_bp = Blueprint('categoria', __name__, template_folder='templates')
producto_bp = Blueprint('producto', __name__, template_folder='templates')

from . import routes