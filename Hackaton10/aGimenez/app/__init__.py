from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Manejador de toda la instancia del login:
login_manager = LoginManager()
# ORM:
db = SQLAlchemy()


# def create_app(settings_module="config.prod"): #para enviar toda la config a amb prod
def create_app(settings_module="config.dev"):  # ambiente
    # Creando instancia de flask:
    app = Flask(__name__, instance_relative_config=True)
    # Cargando config del ambiente
    app.config.from_object(settings_module)

    if app.config.get("TESTING", False):
        app.config.from_pyfile("config-testing.py", silent=True)
    else:
        app.config.from_pyfile("config.py", silent=True)

    # Inicializando login_manager:
    login_manager.init_app(app)
    login_manager.login_view = "login"
    # Inicializando ORM en la app:
    db.init_app(app)

    # Registrando Blueprints (auth, public, products)

    from .auth import auth_bp

    app.register_blueprint(auth_bp)

    from .public import public_bp

    app.register_blueprint(public_bp)

    from .product import product_bp

    app.register_blueprint(product_bp)

    from .venta import venta_bp

    app.register_blueprint(venta_bp)

    register_error_handlers(app)

    return app


# Manejador de errores:
def register_error_handlers(app):
    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template("500.html"), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template("404.html"), 404