import logging
from flask import render_template, redirect, url_for, request, current_app, abort
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from . import cliente_bp
from app.auth.decorators import client_required

from app import login_manager
from app.cajero.models import Factura

logger = logging.getLogger(__name__)


@cliente_bp.route("/cliente/")
@login_required
@client_required
def index():
    facturas = Factura.get_by_cliente(current_user.name)
    return render_template("cliente/index.html", facturas=facturas)

@cliente_bp.route("/cliente/historial/<string:slug>", methods=['GET', 'POST'])
@login_required
@client_required
def show_historial(slug):
    logger.info('Mostrando una factura')
    logger.debug(f'Nro Factura: {slug}')
    factura = Factura.get_by_slug(slug)
    if not factura:
        logger.info(f'La factura {slug} no existe')
        abort(404)
    return render_template("cliente/factura_view.html", factura=factura)
