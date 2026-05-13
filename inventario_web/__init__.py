from flask import Flask

from .routes.historial import historial_bp
from .routes.home import home_bp
from .routes.inventario import inventario_bp
from .routes.productos import productos_bp
from .routes.ventas import ventas_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("inventario_web.config.Config")
    app.register_blueprint(historial_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(inventario_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(ventas_bp)

    return app
