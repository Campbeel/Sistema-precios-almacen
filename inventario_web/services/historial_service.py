def obtener_filtros_historial(request_args):
    return {
        "fecha": (request_args.get("fecha") or "").strip(),
        "tipo_pago": (request_args.get("tipo_pago") or "").strip(),
    }


def listar_historial_ventas(request_args):
    from inventario_web.db import get_connection

    filtros = obtener_filtros_historial(request_args)
    condiciones = []
    parametros = []

    if filtros["fecha"]:
        condiciones.append("DATE(fecha_venta) = %s")
        parametros.append(filtros["fecha"])

    if filtros["tipo_pago"]:
        condiciones.append("tipo_pago = %s")
        parametros.append(filtros["tipo_pago"])

    where_clause = ""
    if condiciones:
        where_clause = f"WHERE {' AND '.join(condiciones)}"

    query_ventas = f"""
        SELECT id, tipo_pago, total, fecha_venta
        FROM ventas_historial
        {where_clause}
        ORDER BY fecha_venta DESC, id DESC
    """

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query_ventas, tuple(parametros))
        ventas = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

    if not ventas:
        return {
            "ventas": [],
            "filtros": filtros,
            "cantidad_ventas": 0,
            "total_mostrado": 0,
        }

    venta_ids = [venta["id"] for venta in ventas]
    placeholders = ", ".join(["%s"] * len(venta_ids))
    query_detalles = f"""
        SELECT
            venta_id,
            codigo_producto,
            nombre_producto,
            cantidad,
            unidad_medida,
            precio_referencia,
            subtotal
        FROM ventas_historial_detalle
        WHERE venta_id IN ({placeholders})
        ORDER BY id ASC
    """

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query_detalles, tuple(venta_ids))
        detalles = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

    detalles_por_venta = {}
    for detalle in detalles:
        detalles_por_venta.setdefault(detalle["venta_id"], []).append(detalle)

    total_mostrado = 0
    for venta in ventas:
        venta["detalles"] = detalles_por_venta.get(venta["id"], [])
        total_mostrado += int(venta["total"])

    return {
        "ventas": ventas,
        "filtros": filtros,
        "cantidad_ventas": len(ventas),
        "total_mostrado": total_mostrado,
    }


def obtener_tipos_pago_historial():
    return (
        {"value": "", "label": "Todos"},
        {"value": "efectivo", "label": "Efectivo"},
        {"value": "tarjeta", "label": "Tarjeta"},
    )
