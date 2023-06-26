from flask import render_template, redirect, url_for
from . import perfil_bp
from flask_login import login_required, current_user
from .forms import PerfilForm
from app.models import Perfil

@perfil_bp.route("/perfil/", methods=['GET', 'POST'])
@login_required
def post_form():
    form = PerfilForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        pais= form.pais.data
        ciudad = form.ciudad.data
        fechaNacimiento = form.fechaNacimiento.data
        info = form.info.data
        avatar = form.avatar.data
        url = form.url.data
        facebook = form.facebook.data
        twitter = form.twitter.data
        perfil = Perfil(user_id = current_user.id, nombre = nombre, apellido = apellido,pais=pais,ciudad=ciudad,fechaNacimiento=fechaNacimiento,info=info,avatar=avatar,url=url,facebook=facebook,twitter=twitter)
        perfil.save()

        return redirect(url_for('public.index'))
    return render_template("perfil/perfil_form.html", form=form)