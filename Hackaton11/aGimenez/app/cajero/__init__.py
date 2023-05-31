from flask import Blueprint

cajero_bp = Blueprint('cajero', __name__, template_folder='templates')

from . import routes
