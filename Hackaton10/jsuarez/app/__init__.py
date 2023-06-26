from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()

#def create_app(settings_module='config.prod'):
def create_app(settings_module='config.dev'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings_module)
    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)
    
    login_manager.init_app(app)
    login_manager.login_view = "login"

    db.init_app(app)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)

    from .perfil import perfil_bp
    app.register_blueprint(perfil_bp)
    register_error_handlers(app)

    from .products import product_bp
    app.register_blueprint(product_bp)
    register_error_handlers(app)

    return app

def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404