from flask import render_template, redirect, url_for
from . import factura_bp
from flask_login import login_required, current_user
from .forms import FacturaForm
from app.models import Factura


@factura_bp.route("/factura/", methods=['GET', 'POST'])
@login_required
def factura_form():
    form = FacturaForm()
    if form.validate_on_submit():
        fecha = form.fecha.data
        cliente_id = form.cliente_id.data
        producto_id = form.producto_id.data
        Cantidad = form.Cantidad.data
        MontoTotal = form.MontoTotal.data
        user_id = current_user.id
        fact = Factura(fecha = fecha, cliente_id = cliente_id, producto_id = producto_id, Cantidad = Cantidad, MontoTotal = MontoTotal, user_id = user_id)
        fact.save()

        facturas = Factura.get_all()

        return render_template("factura/view_factura.html", facturas=facturas)
    return render_template("factura/factura_form.html", form=form)


@factura_bp.route("/factura_all/", methods=['GET'])
@login_required
def factura_all():
    facturas = Factura.get_all()
    return render_template("factura/view_factura.html", facturas=facturas)
