import logging
from flask import render_template, redirect, url_for, abort, request, jsonify
from flask_login import login_required
from app.auth.decorators import cajero_required
from .models import Factura, DetalleFactura
from . import cajero_bp
from .forms import FacturaForm
from app.models import Product

logger = logging.getLogger(__name__)

@cajero_bp.route("/cajero/")
@login_required
@cajero_required
def index():
    return render_template("cajero/index.html")


@cajero_bp.route("/cajero/facturas/")
@login_required
@cajero_required
def list_facturas():
    facturas = Factura.get_all()
    return render_template("cajero/facturas.html", facturas=facturas)


@cajero_bp.route("/cajero/factura/", methods=['GET', 'POST'])
@login_required
@cajero_required
def factura_form():
    form = FacturaForm()
    if form.validate_on_submit():
        numero_factura = form.numero_factura.data
        cliente = form.cliente.data

        factura = Factura(numero_factura=numero_factura, cliente=cliente)

        for producto in form.detalles:
            detalle = DetalleFactura(
                nombre=producto.nombre.data,
                precio=producto.precio.data,
                cantProducto=producto.cantProducto.data

            )
            factura.detalles.append(detalle)

        factura.save()
        logger.info(f'Guardando nueva factura ,{numero_factura}')
        return redirect(url_for("cajero.list_facturas"))
    return render_template("cajero/factura_form.html", form=form)


@cajero_bp.route("/cajero/factura/<int:factura_id>/", methods=['GET', 'POST'])
@login_required
@cajero_required
def update_factura_form(numero_factura):
    """Actualiza una factura existente"""
    factura = Factura.get_by_numero_factura(numero_factura)
    if factura is None:
        logger.info(f'La factura {numero_factura} no existe')
        abort(404)
    # Crea un formulario inicializando los campos con
    # los valores de la factura.
    form = FacturaForm(obj=factura)
    if form.validate_on_submit():
        # Actualiza los campos del post existente
        factura.numero_factura = form.numero_factura.data
        factura.cliente = form.cliente.data
        factura.save()
        logger.info(f'Guardando la factura {numero_factura}')
        return redirect(url_for('cajero.list_facturas'))
    return render_template("cajero/factura_form.html", form=form, factura=factura)


@cajero_bp.route("/cajero/factura/delete/<int:product_id>/", methods=['POST', ])
@login_required
@cajero_required
def delete_factura(numero_factura):
    logger.info(f'Se va a eliminar la factura {numero_factura}')
    factura = Factura.get_by_numero_factura(numero_factura)
    if factura is None:
        logger.info(f'La factura {numero_factura} no existe')
        abort(404)
    factura.delete()
    logger.info(f'La factura {numero_factura} ha sido eliminado')
    return redirect(url_for('cajero.list_facturas'))


@cajero_bp.route("/cajero/buscar_producto", methods=['POST'])
@login_required
@cajero_required
def buscar_producto():
    nombre = request.form.get('nombre')
    logger.info(f'producto nombre {nombre}')
    producto = Product.get_by_slug(nombre)
    logger.info(f'producto {producto}')
    if producto:
        response = {
            'precio': producto.precio
        }
    else:
        response = {
            'error': 'Producto no encontrado'
        }

    return jsonify(response)

@cajero_bp.route("/cajero/factura/<string:slug>/", methods=['GET', 'POST'])
@login_required
@cajero_required
def show_factura(slug):
    logger.info('Mostrando una factura')
    logger.debug(f'Nro Factura: {slug}')
    factura = Factura.get_by_slug(slug)
    if not factura:
        logger.info(f'La factura {slug} no existe')
        abort(404)
    return render_template("cajero/factura_view.html", factura=factura)