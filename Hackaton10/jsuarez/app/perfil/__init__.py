from flask import Blueprint

perfil_bp = Blueprint('perfil', __name__, template_folder='templates')

from . import routes