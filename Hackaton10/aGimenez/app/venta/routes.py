from flask import render_template, redirect, url_for
from . import venta_bp
from flask_login import login_required, current_user
from .forms import VentaForm
from app.models import Product, Venta


@venta_bp.route("/venta/", methods=["GET", "POST"])
@login_required
def venta_form():
    form = VentaForm()

    if form.validate_on_submit():
        fechaVenta = form.fechaVenta.data
        nombre = form.nombre.data
        categoria = form.categoria.data
        stock = form.stock.data
        precioUnitario = form.precioUnitario.data
        subTotal = form.subTotal.data

        venta = Venta(fechaVenta=fechaVenta, nombre=nombre, categoria=categoria, stock=stock, precioUnitario=precioUnitario, subTotal=subTotal)
        venta.save()

        return redirect(url_for("public.index"))
    return render_template("venta/ventas_form.html", form=form)