from flask import abort, render_template
from werkzeug.exceptions import NotFound
from app.models import Product

from . import public_bp


@public_bp.route("/")
def index():
    return render_template("public/index.html")


@public_bp.route("/product/<int:id>/")
def show_product(id):
    product = Product.get_by_id(id)
    if product is None:
        raise NotFound(id)
    return render_template("public/product_view.html", product=product)
