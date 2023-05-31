from flask import Flask, render_template, request, redirect, url_for, abort
from . import cliente_bp
from flask_login import login_required, current_user
from app.auth.decorators import admin_required
from .forms import ClienteForm
from app.models import Cliente
from werkzeug.exceptions import NotFound

@cliente_bp.route("/cliente/", methods=['GET', 'POST'])
@login_required
def cliente_form():
    form = ClienteForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        dni = form.dni.data
        celular = form.celular.data
        direccion = form.direccion.data
        cliente = Cliente(nombre = nombre, dni = dni, celular = celular, direccion = direccion)
        cliente.save()

        clientes = Cliente.get_all()

        return render_template("view_cliente.html", clientes=clientes)
    return render_template("cliente_form.html", form=form)
