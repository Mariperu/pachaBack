from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many, belongs_to_many


DEBUG = True
ORATOR_DATABASES = {
    "default": "postgres",
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "user": "postgres",
        "password": 'admin',
        "database": "bd_a1703782",
    },
}


app = Flask(__name__)
app.config.from_object(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False

db = Orator(app)

class Alumno(db.Model):
    __fillable__ = ["id", "identificador", "nombre", "edad","correo"]
    __table__ = 'alumno' #Cuando defines un modelo en Flask-SQLAlchemy, si no especificas la propiedad __table__, SQLAlchemy generará automáticamente el nombre de la tabla a partir del nombre de la clase del modelo en minúsculas y pluralizada. Por ejemplo, si tienes una clase Alumno, el nombre de la tabla se generará como "alumnos". Sin embargo, en ocasiones, es posible que desees especificar un nombre de tabla personalizado.

class Profesor(db.Model):
    __fillable__ = ["id", "identificador", "nombre", "edad","correo"]
    __table__ = 'profesor'

class Curso(db.Model):
    __fillable__ = ["id", "nombre","identificador"]
    __table__ = 'curso'

    @belongs_to_many
    def alumnos(self):
        return Alumno

    @belongs_to_many
    def profesores(self):
        return Profesor


class Salon(db.Model):
    __fillable__ = ["id","identificador","nombre", "anioescolar"]
    __table__ = 'salon'

    # @belongs_to_many
    # def cursos(self):
    #     return Curso


@app.route("/crear-alumno", methods=["POST"])
def create_alumno():
    req = Alumno.create(**request.get_json())
    return jsonify(req)


@app.route("/listar-alumnos", methods=["GET"])
def get_alumnos():
    req = Alumno.all()
    return jsonify(req)


@app.route("/alumnos/<int:alumno_id>", methods=["PATCH"])
def update_alumno(alumno_id):
    req = Alumno.find_or_fail(alumno_id)
    req.update(**request.get_json())
    return jsonify(req)


@app.route("/alumnos/<int:alumno_id>", methods=["DELETE"])
def delete_alumno(alumno_id):
    req = Alumno.find_or_fail(alumno_id)
    req.delete()
    return app.response_class("No Content", 204)


@app.route("/crear-profesor", methods=["POST"])
def create_profesor():
    req = Profesor.create(**request.get_json())
    return jsonify(req)


@app.route("/listar-profesores", methods=["GET"])
def get_profesores():
    req = Profesor.all()
    return jsonify(req)


@app.route("/profesores/<int:profesor_id>", methods=["PATCH"])
def update_profesor(profesor_id):
    req = Profesor.find_or_fail(profesor_id)
    req.update(**request.get_json())
    return jsonify(req)


@app.route("/profesores/<int:profesor_id>", methods=["DELETE"])
def delete_profesor(profesor_id):
    req = Profesor.find_or_fail(profesor_id)
    req.delete()
    return app.response_class("No Content", 204)


@app.route("/crear-curso", methods=["POST"])
def create_curso():
    req = Curso.create(**request.get_json())
    return jsonify(req)


@app.route("/listar-cursos", methods=["GET"])
def get_cursos():
    req = Curso.all()
    return jsonify(req)


@app.route("/cursos/<int:curso_id>", methods=["PATCH"])
def update_curso(curso_id):
    req = Curso.find_or_fail(curso_id)
    req.update(**request.get_json())
    return jsonify(req)


@app.route("/cursos/<int:curso_id>", methods=["DELETE"])
def delete_curso(curso_id):
    req = Curso.find_or_fail(curso_id)
    req.delete()
    return app.response_class("No Content", 204)


@app.route("/crear-salon", methods=["POST"])
def create_salon():
    req = Salon.create(**request.get_json())
    return jsonify(req)


@app.route("/listar-salones", methods=["GET"])
def get_salones():
    req = Salon.all()
    return jsonify(req)


@app.route("/salones/<int:salon_id>", methods=["PATCH"])
def update_salon(salon_id):
    req = Salon.find_or_fail(salon_id)
    req.update(**request.get_json())
    return jsonify(req)

@app.route("/salones/<int:salon_id>", methods=["PATCH"])
def delete_salon(salon_id):
    req = Salon.find_or_fail(salon_id)
    req.delete()
    return jsonify(req)

if __name__ == "__main__":
    app.run()