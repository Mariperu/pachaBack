import logging
from flask import render_template, redirect, url_for, abort, request, current_app
from flask_login import login_required, current_user
from flask_login import current_user, login_user, logout_user

from app.auth.decorators import almacen_required
from app.models import Product
from app.almacen import almacen_bp
from .forms import ProductForm

logger = logging.getLogger(__name__)

@almacen_bp.route("/almacen/")
@login_required
@almacen_required
def index():
    return render_template("almacen/index.html")


@almacen_bp.route("/almacen/products/")
@login_required
@almacen_required
def list_products():
    products = Product.get_all()
    return render_template("almacen/products.html", products=products)

@almacen_bp.route("/almacen/product/", methods=['GET', 'POST'])
@login_required
@almacen_required
def product_form():
    """Crea un nuevo post"""
    form = ProductForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        stock = form.stock.data
        precio = form.precio.data

        product = Product(nombre=nombre, stock=stock, precio=precio)

        product.save()
        logger.info(f'Guardando nuevo product {nombre}')
        return redirect(url_for('almacen.list_products'))
    return render_template("almacen/product_form.html", form=form)

@almacen_bp.route("/almacen/product/<int:product_id>/", methods=['GET', 'POST'])
@login_required
@almacen_required
def update_product_form(product_id):
    """Actualiza un product existente"""
    product = Product.get_by_id(product_id)
    if product is None:
        logger.info(f'El product {product_id} no existe')
        abort(404)
    # Crea un formulario inicializando los campos con
    # los valores del product.
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        # Actualiza los campos del post existente
        product.nombre = form.nombre.data
        product.stock = form.stock.data
        product.precio = form.precio.data
        product.save()
        logger.info(f'Guardando el product {product_id}')
        return redirect(url_for('almacen.list_products'))
    return render_template("almacen/product_form.html", form=form, product=product)

@almacen_bp.route("/almacen/product/delete/<int:product_id>/", methods=['POST', ])
@login_required
@almacen_required
def delete_product(product_id):
    logger.info(f'Se va a eliminar el product {product_id}')
    product = Product.get_by_id(product_id)
    if product is None:
        logger.info(f'El product {product_id} no existe')
        abort(404)
    product.delete()
    logger.info(f'El product {product_id} ha sido eliminado')
    return redirect(url_for('almacen.list_products'))
