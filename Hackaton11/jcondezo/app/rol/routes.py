from flask import Flask, render_template, request, redirect, url_for, abort
from . import rol_bp
from flask_login import login_required, current_user
from app.auth.decorators import admin_required
from .forms import RolForm
from app.models import Rol
from werkzeug.exceptions import NotFound

@rol_bp.route("/rol/", methods=['GET', 'POST'])
@login_required
@admin_required
def rol_form():
    form = RolForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        rol = Rol(nombre = nombre)
        rol.save()

        roles = Rol.get_all()

        return render_template("view_rol.html", roles=roles)
    return render_template("rol_form.html", form=form)
