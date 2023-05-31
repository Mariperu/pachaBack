from flask import abort, render_template
from werkzeug.exceptions import NotFound
from app.models import Product, Venta

from . import public_bp

products = []
ventas = []
@public_bp.route("/")
def index():
    return render_template("public/index.html")


@public_bp.route("/products/", methods=['GET', 'POST'])
def show_products():
    return render_template("public/products.html", products=products)

@public_bp.route("/product/<int:id>/")
def show_product(id):
    product = Product.get_by_id(id)
    if product is None:
        raise NotFound(id)
    return render_template("public/producto_view.html", product=product)

@public_bp.route("/ventas/", methods=['GET', 'POST'])
def show_ventas():
    return render_template("public/ventas.html", ventas=ventas)

@public_bp.route("/venta/<int:id>/")
def show_venta(id):
    venta = Venta.get_by_id(id)
    if venta is None:
        raise NotFound(id)
    return render_template("public/venta_view.html", venta=venta)