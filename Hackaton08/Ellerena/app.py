from flask import Flask, request
from flask_orator import Orator, jsonify


#Configuration
DEBUG = True
ORATOR_DATABASES = {
    'default': 'twittor',
    'twittor': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': '123',
        'database': 'tarea08'
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

db = Orator(app)

class Alumno(db.Model):
    __fillable__ = ['nombre', 'identificador','edad','email']


@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = Alumno.all()
    return jsonify(alumnos)

@app.route('/profesores', methods=['GET'])
def profesores():
    alumnos = profesores.all()
    return jsonify(profesores)

if __name__ == '__main__':
    app.run()