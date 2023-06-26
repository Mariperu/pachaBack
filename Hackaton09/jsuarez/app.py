from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, logout_user, current_user, login_user, login_required
from werkzeug.urls import url_parse

from forms import SignupForm, LoginForm, AlumnoForm, ProfesorForm, CursoForm, SalonForm
from models import users, get_user, User, Alumnos, Profesores, Cursos, Salones

# Configuración para archivos estáticos
app = Flask(__name__)

# Configuración para archivos estáticos
app.static_folder = 'static'

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

login_manager = LoginManager(app)
login_manager.login_view = "login"

posts = []
alumnos = []
profesores = []
salones = []
cursos = []

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)

# Ruta Alumnos
@app.route("/alumnos/")
def show_alumnos():
    return render_template("public/alumnos.html", alumnos=alumnos)

@app.route("/admin/alumnos/", methods=['GET', 'POST'], defaults={'id_alumno': None})
@app.route("/admin/alumnos/<int:id_alumno>/", methods=['GET', 'POST'])
@login_required
def post_form(id_alumno):
    form = AlumnoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        edad = form.edad.data
        correo = form.correo.data
        identificador = form.identificador.data

        alumno = {'nombre': nombre, 'edad': edad, 'identificador': identificador, 'correo' : correo}
        alumnos.append(alumno)

        return redirect(url_for('index'))
    return render_template("admin/alumno_form.html", form=form)

#Ruta Profesor
@app.route("/profesores/")
def show_profesores():
    return render_template("public/profesores.html", profesores=profesores)
@app.route("/admin/profesores/", methods=['GET', 'POST'], defaults={'id_profesor': None})
@app.route("/admin/profesores/<int:id_profesor>/", methods=['GET', 'POST'])
@login_required
def post_form2(id_profesor):
    form = ProfesorForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        edad = form.edad.data
        correo = form.correo.data
        identificador = form.identificador.data

        profesor = {'nombre': nombre, 'edad': edad, 'identificador': identificador, 'correo' : correo}
        profesores.append(profesor)

        return redirect(url_for('index'))
    return render_template("admin/profesor_form.html", form=form)

# Ruta Curso
@app.route("/cursos/")
def show_cursos():
    return render_template("public/cursos.html", cursos=cursos)
@app.route("/admin/cursos/", methods=['GET', 'POST'], defaults={'id_curso': None})
@app.route("/admin/cursos/<int:id_curso>/", methods=['GET', 'POST'])
@login_required
def post_form3(id_curso):
    form = CursoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        identificador = form.identificador.data

        curso = {'nombre': nombre, 'identificador': identificador}
        cursos.append(curso)

        return redirect(url_for('index'))
    return render_template("admin/curso_form.html", form=form)

# Ruta Salon
@app.route("/salones/")
def show_salones():
    return render_template("public/salones.html", salones=salones)
@app.route("/admin/salones/", methods=['GET', 'POST'], defaults={'id_salon': None})
@app.route("/admin/salones/<int:id_salon>/", methods=['GET', 'POST'])
@login_required
def post_form4(id_salon):
    form = SalonForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        anioEscolar = form.anioEscolar.data

        salon = {'nombre': nombre, 'anioEscolar': anioEscolar}
        salones.append(salon)

        return redirect(url_for('index'))
    return render_template("admin/salon_form.html", form=form)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, email, password)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("signup_form.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)