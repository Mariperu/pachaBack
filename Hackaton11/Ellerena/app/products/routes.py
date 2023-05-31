from flask import render_template, redirect, url_for
from . import product_bp
from flask_login import login_required
from .forms import ProductForm
from app.models import Product

@product_bp.route("/product/", methods=['GET', 'POST'])
@login_required
def post_form():
    form = ProductForm()
    if form.validate_on_submit():
        producto = form.producto.data
        stock = form.stock.data
        precio= form.precio.data
        product = Product(id = id, producto = producto, stock = stock, precio = precio)
        product.save()

        return redirect(url_for('public.index'))
    return render_template("product/product_form.html", form=form)