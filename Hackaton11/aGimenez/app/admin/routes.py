import logging
from flask import render_template, redirect, url_for, abort
from flask_login import login_required
from app.auth.decorators import admin_required
from app.models import Product
from . import admin_bp
from .forms import ProductForm, UserAdminForm
from app.auth.models import User
from app.cajero.models import Factura
from app.cajero.forms import FacturaForm

logger = logging.getLogger(__name__)


@admin_bp.route("/admin/")
@login_required
@admin_required
def index():
    return render_template("admin/index.html")

@admin_bp.route("/admin/products/")
@login_required
@admin_required
def list_products():
    products = Product.get_all()
    return render_template("admin/products.html", products=products)


@admin_bp.route("/admin/users/")
@login_required
@admin_required
def list_users():
    users = User.get_all()
    return render_template("admin/users.html", users=users)


@admin_bp.route("/admin/user/<int:user_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def update_user_form(user_id):
    # Aquí entra para actualizar un usuario existente
    user = User.get_by_id(user_id)
    if user is None:
        logger.info(f'El usuario {user_id} no existe')
        abort(404)
    # Crea un formulario inicializando los campos con
    # los valores del usuario.
    form = UserAdminForm(obj=user)
    if form.validate_on_submit():
        # Actualiza los campos del usuario existente
        user.rol = form.rol.data
        user.save()
        logger.info(f'Guardando el usuario {user_id}')
        return redirect(url_for('admin.list_users'))
    return render_template("admin/user_form.html", form=form, user=user)


@admin_bp.route("/admin/user/delete/<int:user_id>/", methods=['POST', ])
@login_required
@admin_required
def delete_user(user_id):
    logger.info(f'Se va a eliminar al usuario {user_id}')
    user = User.get_by_id(user_id)
    if user is None:
        logger.info(f'El usuario {user_id} no existe')
        abort(404)
    user.delete()
    logger.info(f'El usuario {user_id} ha sido eliminado')
    return redirect(url_for('admin.list_users'))

@admin_bp.route("/admin/facturas/")
@login_required
@admin_required
def list_facturas():
    facturas = Factura.get_all()
    return render_template("admin/facturas.html", facturas=facturas)

@admin_bp.route("/admin/factura/<string:slug>/", methods=['GET', 'POST'])
@login_required
@admin_required
def show_factura(slug):
    logger.info('Mostrando una factura')
    logger.debug(f'Nro Factura: {slug}')
    factura = Factura.get_by_slug(slug)
    if not factura:
        logger.info(f'La factura {slug} no existe')
        abort(404)
    return render_template("admin/factura_view.html", factura=factura)