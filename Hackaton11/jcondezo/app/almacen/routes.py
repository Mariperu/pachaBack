from flask import render_template, redirect, url_for
from . import producto_bp, categoria_bp
from flask_login import login_required, current_user
from .forms import ProductoForm, CategoriaForm
from app.models import Producto, Categoria


@categoria_bp.route("/categorias/", methods=['GET', 'POST'])
@login_required
def categoria_form():
    form = CategoriaForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        categ = Categoria(nombre = nombre, descripcion = descripcion)
        categ.save()

        categorias = Categoria.get_all()

        return render_template("categoria/view_categoria.html", categorias=categorias)
    return render_template("categoria/categoria_form.html", form=form)


@producto_bp.route("/productos/", methods=['GET', 'POST'])
@login_required
def productos_form():
    form = ProductoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        cantidad = form.cantidad.data
        marca = form.marca.data
        precio = form.precio.data
        categoria_id = form.categoria_id.data
        prod = Producto(nombre = nombre, descripcion = descripcion, cantidad = cantidad, marca = marca, precio = precio, categoria_id = categoria_id)
        prod.save()

        productos = Producto.get_all()

        return render_template("producto/view_producto.html", productos=productos)
    return render_template("producto/producto_form.html", form=form)


@producto_bp.route("/productos_all/", methods=['GET'])
@login_required
def productos_all():
    productos = Producto.get_all()
    return render_template("producto/view_producto.html", productos=productos)
