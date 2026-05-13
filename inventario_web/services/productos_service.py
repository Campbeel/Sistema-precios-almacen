from mysql.connector import Error

from inventario_web.db import get_connection
from inventario_web.productos_config import (
    DEFAULT_PRODUCT_TYPE,
    PRODUCTOS_CONFIG,
)


def obtener_tipos_producto():
    return PRODUCTOS_CONFIG


def obtener_tipo_config(tipo_producto):
    return PRODUCTOS_CONFIG.get(tipo_producto, PRODUCTOS_CONFIG[DEFAULT_PRODUCT_TYPE])


def listar_productos(tipo_producto):
    config = obtener_tipo_config(tipo_producto)
    columnas = ["id", config["code_field"], "nombre", config["price_field"], "activo"]
    if config["has_quantity"]:
        columnas.insert(4, "cantidad")

    query = f"SELECT {', '.join(columnas)} FROM {config['table']} ORDER BY nombre ASC"

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()


def obtener_producto_por_id(tipo_producto, producto_id):
    config = obtener_tipo_config(tipo_producto)
    query = f"SELECT * FROM {config['table']} WHERE id = %s"

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, (producto_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        connection.close()


def crear_producto(tipo_producto, form_data):
    config = obtener_tipo_config(tipo_producto)
    campos = [config["code_field"], "nombre", config["price_field"]]
    valores = [form_data[config["code_field"]], form_data["nombre"], form_data[config["price_field"]]]

    if config["has_quantity"]:
        campos.append("cantidad")
        valores.append(int(form_data["cantidad"]))

    placeholders = ", ".join(["%s"] * len(campos))
    query = f"INSERT INTO {config['table']} ({', '.join(campos)}) VALUES ({placeholders})"

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, tuple(valores))
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def actualizar_producto(tipo_producto, producto_id, form_data):
    config = obtener_tipo_config(tipo_producto)
    asignaciones = [
        f"{config['code_field']} = %s",
        "nombre = %s",
        f"{config['price_field']} = %s",
    ]
    valores = [form_data[config["code_field"]], form_data["nombre"], form_data[config["price_field"]]]

    if config["has_quantity"]:
        asignaciones.append("cantidad = %s")
        valores.append(int(form_data["cantidad"]))

    valores.append(producto_id)
    query = f"UPDATE {config['table']} SET {', '.join(asignaciones)} WHERE id = %s"

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, tuple(valores))
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def eliminar_producto(tipo_producto, producto_id):
    config = obtener_tipo_config(tipo_producto)
    query = f"DELETE FROM {config['table']} WHERE id = %s"

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, (producto_id,))
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def validar_formulario(tipo_producto, form_data):
    config = obtener_tipo_config(tipo_producto)
    errores = []

    if not form_data.get(config["code_field"], "").strip():
        errores.append(f"El campo {config['code_label']} es obligatorio.")

    if not form_data.get("nombre", "").strip():
        errores.append("El nombre es obligatorio.")

    precio = form_data.get(config["price_field"], "").strip()
    if not precio:
        errores.append(f"El campo {config['price_label']} es obligatorio.")
    else:
        try:
            if float(precio) < 0:
                errores.append(f"El campo {config['price_label']} no puede ser negativo.")
        except ValueError:
            errores.append(f"El campo {config['price_label']} debe ser numerico.")

    if config["has_quantity"]:
        cantidad = form_data.get("cantidad", "").strip()
        if not cantidad:
            errores.append("La cantidad es obligatoria.")
        else:
            try:
                if int(cantidad) < 0:
                    errores.append("La cantidad no puede ser negativa.")
            except ValueError:
                errores.append("La cantidad debe ser un numero entero.")

    return errores


def es_error_bd_duplicado(error):
    return isinstance(error, Error) and error.errno == 1062
