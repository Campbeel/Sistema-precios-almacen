from flask import Blueprint, render_template, request
from mysql.connector import Error

from inventario_web.services.historial_service import (
    listar_historial_ventas,
    obtener_filtros_historial,
    obtener_tipos_pago_historial,
)


historial_bp = Blueprint("historial", __name__, url_prefix="/historial-ventas")


@historial_bp.route("/", methods=["GET"])
def historial_ventas_view():
    error_carga = None
    data = {
        "ventas": [],
        "filtros": obtener_filtros_historial(request.args),
        "cantidad_ventas": 0,
        "total_mostrado": 0,
    }

    try:
        data = listar_historial_ventas(request.args)
    except Error:
        error_carga = (
            "No fue posible cargar el historial de ventas. "
            "Revisa que las tablas del historial existan en MySQL."
        )

    return render_template(
        "historial/lista.html",
        ventas=data["ventas"],
        filtros=data["filtros"],
        cantidad_ventas=data["cantidad_ventas"],
        total_mostrado=data["total_mostrado"],
        tipos_pago=obtener_tipos_pago_historial(),
        error_carga=error_carga,
    )
