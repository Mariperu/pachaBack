from flask import Flask, request
from flask_orator import Orator, jsonify
from modelos import User

#Configuration
DEBUG = True
ORATOR_DATABASES = {
    'default': 'twittor',
    'twittor': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': 'pacha23',
        'database': 'twittor'
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)

# Initializing Orator
db = Orator(app)

if __name__ == '__main__':
    app.run()

# Modelos
class User(db.Model):
    __fillable__ = ['name','email']

# Agregar ruta para crear usuarios
@app.route('/users', methods=['POST'])
def create_user():
    user = User.create(**request.get_json())

    return jsonify(user)