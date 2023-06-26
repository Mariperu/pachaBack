from flask import render_template, redirect, url_for
from . import product_bp
from flask_login import login_required, current_user
from .forms import ProductForm
from app.models import Product


@product_bp.route("/product/", methods=["GET", "POST"])
@login_required
def product_form():
    form = ProductForm()

    if form.validate_on_submit():
        nombre = form.nombre.data
        categoria = form.categoria.data
        stock = form.stock.data
        precioUnitario = form.precioUnitario.data

        product = Product(nombre=nombre, categoria=categoria, stock=stock, precioUnitario=precioUnitario)
        product.save()

        return redirect(url_for("public.index"))
    return render_template("product/productos_form.html", form=form)