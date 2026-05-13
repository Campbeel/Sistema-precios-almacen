from flask import Blueprint, render_template
from mysql.connector import Error

from inventario_web.services.consultas_service import obtener_resumen_inventario


inventario_bp = Blueprint("inventario", __name__, url_prefix="/inventario")


@inventario_bp.route("/resumen", methods=["GET"])
def resumen_inventario_view():
    resumen = []
    error_carga = None
    try:
        resumen = obtener_resumen_inventario()
    except Error:
        error_carga = (
            "No fue posible cargar el resumen de inventario. "
            "Revisa la conexion a MySQL."
        )

    return render_template(
        "inventario/resumen.html",
        resumen=resumen,
        error_carga=error_carga,
    )
