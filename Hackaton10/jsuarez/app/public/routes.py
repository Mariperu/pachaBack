from flask import abort, render_template
from werkzeug.exceptions import NotFound
from app.models import Perfil

from . import public_bp


@public_bp.route("/")
def index():
    return render_template("public/index.html")


@public_bp.route("/perfil/<int:id>/")
def show_perfil(id):
    perfil = Perfil.get_by_id(id)
    if perfil is None:
        raise NotFound(id)
    return render_template("public/perfil_view.html", perfil=perfil)
