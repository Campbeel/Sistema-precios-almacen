from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from mysql.connector import Error

from inventario_web.db import get_connection
from inventario_web.productos_config import PRODUCTOS_CONFIG


PRODUCT_SEARCH_ORDER = ("codigo_barra", "sin_codigo", "granel")
PAYMENT_TYPES = {"efectivo", "tarjeta"}
ZERO = 0


def buscar_producto_por_codigo(codigo):
    codigo = codigo.strip()
    if not codigo:
        return None

    for tipo_producto in PRODUCT_SEARCH_ORDER:
        config = PRODUCTOS_CONFIG[tipo_producto]
        columnas = [
            "id",
            f"{config['code_field']} AS codigo",
            "nombre",
            f"{config['price_field']} AS precio",
            "activo",
        ]
        if config["has_quantity"]:
            columnas.append("cantidad")

        query = (
            f"SELECT {', '.join(columnas)} "
            f"FROM {config['table']} "
            f"WHERE {config['code_field']} = %s AND activo = 1"
        )

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (codigo,))
            producto = cursor.fetchone()
        finally:
            cursor.close()
            connection.close()

        if producto:
            return _normalizar_producto(tipo_producto, producto)

    return None


def preparar_producto_para_venta(codigo):
    producto = buscar_producto_por_codigo(codigo)
    if not producto:
        return None, "Producto no encontrado para el codigo ingresado."
    return producto, None


def obtener_carrito_vacio():
    return []


def obtener_total_carrito(carrito):
    total = ZERO
    for item in carrito:
        total += int(item["subtotal"])
    return total


def agregar_producto_al_carrito(carrito, codigo, cantidad_raw):
    producto = buscar_producto_por_codigo(codigo)
    if not producto:
        return carrito, "Producto no encontrado para el codigo ingresado."

    cantidad = _parsear_cantidad(producto, cantidad_raw)
    if cantidad is None:
        return carrito, "La cantidad ingresada no es valida para este tipo de producto."

    if producto["has_stock_control"]:
        cantidad_en_carrito = _obtener_cantidad_en_carrito(
            carrito, producto["tipo_producto"], producto["id"]
        )
        disponible = int(producto["cantidad_disponible"])
        if cantidad_en_carrito + cantidad > disponible:
            return carrito, "No hay stock suficiente para agregar esa cantidad."

    carrito_actualizado = list(carrito)
    indice_existente = _buscar_item_en_carrito(
        carrito_actualizado, producto["tipo_producto"], producto["id"]
    )

    if indice_existente is not None:
        item = carrito_actualizado[indice_existente]
        nueva_cantidad = int(item["quantity"]) + cantidad
        carrito_actualizado[indice_existente] = _crear_item_carrito(producto, nueva_cantidad)
    else:
        carrito_actualizado.append(_crear_item_carrito(producto, cantidad))

    return carrito_actualizado, None


def eliminar_item_del_carrito(carrito, index):
    carrito_actualizado = list(carrito)
    if 0 <= index < len(carrito_actualizado):
        carrito_actualizado.pop(index)
    return carrito_actualizado


def obtener_tipos_pago():
    return (
        {"value": "efectivo", "label": "Efectivo"},
        {"value": "tarjeta", "label": "Tarjeta"},
    )


def finalizar_venta(carrito, tipo_pago):
    if not carrito:
        return "No hay productos cargados en la venta."
    if tipo_pago not in PAYMENT_TYPES:
        return "Debes seleccionar un tipo de pago valido."

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        total_venta = obtener_total_carrito(carrito)

        for item in carrito:
            if not item["has_stock_control"]:
                continue

            config = PRODUCTOS_CONFIG[item["tipo_producto"]]
            query = (
                f"SELECT cantidad FROM {config['table']} "
                f"WHERE id = %s AND activo = 1 FOR UPDATE"
            )
            cursor.execute(query, (item["product_id"],))
            producto = cursor.fetchone()

            if not producto:
                connection.rollback()
                return f"El producto {item['name']} ya no esta disponible."

            stock_actual = int(producto["cantidad"])
            cantidad_vendida = int(item["quantity"])
            if cantidad_vendida > stock_actual:
                connection.rollback()
                return f"No hay stock suficiente para {item['name']}."

            nuevo_stock = stock_actual - cantidad_vendida
            update_query = f"UPDATE {config['table']} SET cantidad = %s WHERE id = %s"
            cursor.execute(update_query, (nuevo_stock, item["product_id"]))

        cursor.execute(
            """
            INSERT INTO ventas_historial (tipo_pago, total)
            VALUES (%s, %s)
            """,
            (tipo_pago, total_venta),
        )
        venta_id = cursor.lastrowid

        detalle_query = """
            INSERT INTO ventas_historial_detalle (
                venta_id,
                tipo_producto,
                producto_id,
                codigo_producto,
                nombre_producto,
                cantidad,
                unidad_medida,
                precio_referencia,
                subtotal
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for item in carrito:
            cursor.execute(
                detalle_query,
                (
                    venta_id,
                    item["tipo_producto"],
                    item["product_id"],
                    item["code"],
                    item["name"],
                    int(item["quantity"]),
                    item["quantity_label"],
                    int(item["unit_price"]),
                    int(item["subtotal"]),
                ),
            )

        connection.commit()
        return None
    except Error:
        connection.rollback()
        return "No fue posible registrar la venta en la base de datos."
    finally:
        cursor.close()
        connection.close()


def _normalizar_producto(tipo_producto, producto):
    config = PRODUCTOS_CONFIG[tipo_producto]
    precio = Decimal(str(producto["precio"]))
    cantidad_disponible = producto.get("cantidad")
    is_granel = not config["has_quantity"]
    return {
        "tipo_producto": tipo_producto,
        "id": producto["id"],
        "codigo": str(producto["codigo"]),
        "nombre": producto["nombre"],
        "precio": precio,
        "precio_mostrable": _round_clp_to_10(precio),
        "price_label": config["price_label"],
        "has_stock_control": config["has_quantity"],
        "cantidad_disponible": cantidad_disponible,
        "is_granel": is_granel,
        "sale_input_label": "Peso en gramos" if is_granel else "Cantidad en unidades",
        "sale_input_placeholder": "Ej: 500" if is_granel else "Ej: 2",
        "sale_input_step": "1",
        "sale_input_min": "1",
        "quantity_label": "gr" if is_granel else "unidades",
    }


def _parsear_cantidad(producto, cantidad_raw):
    cantidad_raw = (cantidad_raw or "").strip()
    if not cantidad_raw:
        cantidad_raw = "1"

    try:
        cantidad = Decimal(cantidad_raw)
    except InvalidOperation:
        return None

    if cantidad <= 0:
        return None

    if cantidad != cantidad.to_integral_value():
        return None

    return int(cantidad)


def _obtener_cantidad_en_carrito(carrito, tipo_producto, product_id):
    for item in carrito:
        if item["tipo_producto"] == tipo_producto and item["product_id"] == product_id:
            return int(item["quantity"])
    return ZERO


def _buscar_item_en_carrito(carrito, tipo_producto, product_id):
    for index, item in enumerate(carrito):
        if item["tipo_producto"] == tipo_producto and item["product_id"] == product_id:
            return index
    return None


def _crear_item_carrito(producto, cantidad):
    if producto["is_granel"]:
        subtotal_base = producto["precio"] * (Decimal(cantidad) / Decimal("1000"))
    else:
        subtotal_base = producto["precio"] * Decimal(cantidad)

    subtotal = _round_clp_to_10(subtotal_base)
    unit_price = _round_clp_to_10(producto["precio"])

    return {
        "tipo_producto": producto["tipo_producto"],
        "product_id": producto["id"],
        "code": producto["codigo"],
        "name": producto["nombre"],
        "quantity": str(int(cantidad)),
        "quantity_label": producto["quantity_label"],
        "unit_price": str(unit_price),
        "unit_price_label": producto["price_label"],
        "subtotal": str(subtotal),
        "has_stock_control": producto["has_stock_control"],
    }


def _round_clp_to_10(value):
    rounded_to_peso = int(Decimal(value).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    residue = rounded_to_peso % 10
    if residue <= 4:
        return rounded_to_peso - residue
    return rounded_to_peso + (10 - residue)
