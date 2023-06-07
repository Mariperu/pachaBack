from flask import Flask
from django.core.wsgi import get_wsgi_application


app = Flask(__name__)

# Configuración de Django
app.wsgi_app = get_wsgi_application()

# Rutas de Flask
@app.route('/')
def index():
    return '¡Bienvenido al sistema del colegio!'

# Agrega las rutas adicionales que sean necesarias

if __name__ == '__main__':
    app.run(debug=True)

