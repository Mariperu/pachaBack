from flask import Blueprint

rol_bp = Blueprint('rol', __name__, template_folder='templates')

from . import routes