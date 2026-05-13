from flask import Flask, redirect, url_for

from .routes.productos import productos_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("inventario_web.config.Config")
    app.register_blueprint(productos_bp)

    @app.route("/")
    def index():
        return redirect(url_for("productos.listar_productos_view"))

    return app
