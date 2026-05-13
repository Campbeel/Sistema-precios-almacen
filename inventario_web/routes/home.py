from flask import Blueprint, render_template, url_for


home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def landing_view():
    opciones = [
        {
            "titulo": "Inventario",
            "descripcion": "Ingresar, editar o eliminar productos del sistema.",
            "url": url_for("productos.listar_productos_view"),
            "cta": "Ir a inventario",
        },
        {
            "titulo": "Inventario total",
            "descripcion": "Consultar cantidades y precios de todo el inventario cargado.",
            "url": url_for("inventario.resumen_inventario_view"),
            "cta": "Ver resumen",
        },
        {
            "titulo": "Venta",
            "descripcion": "Cargar productos por codigo y ver el total acumulado de la venta.",
            "url": url_for("ventas.venta_view"),
            "cta": "Abrir venta",
        },
    ]
    return render_template("landing.html", opciones=opciones)
