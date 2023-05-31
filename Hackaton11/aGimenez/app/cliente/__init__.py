from flask import Blueprint

cliente_bp = Blueprint('cliente', __name__, template_folder='templates')

from . import routes