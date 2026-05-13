from inventario_web.db import get_connection
from inventario_web.productos_config import PRODUCTOS_CONFIG


def obtener_resumen_inventario():
    resumen = []

    for tipo_producto, config in PRODUCTOS_CONFIG.items():
        columnas = [
            "id",
            f"{config['code_field']} AS codigo",
            "nombre",
            f"{config['price_field']} AS precio",
        ]

        if config["has_quantity"]:
            columnas.append("cantidad")

        query = (
            f"SELECT {', '.join(columnas)} "
            f"FROM {config['table']} "
            f"WHERE activo = 1 "
            f"ORDER BY nombre ASC"
        )

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query)
            productos = cursor.fetchall()
        finally:
            cursor.close()
            connection.close()

        resumen.append(
            {
                "tipo": tipo_producto,
                "titulo": config["label"],
                "code_label": config["code_label"],
                "price_label": config["price_label"],
                "has_quantity": config["has_quantity"],
                "productos": productos,
            }
        )

    return resumen
