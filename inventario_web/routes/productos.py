from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from mysql.connector import Error

from inventario_web.productos_config import DEFAULT_PRODUCT_TYPE
from inventario_web.services.productos_service import (
    actualizar_producto,
    crear_producto,
    eliminar_producto,
    es_error_bd_duplicado,
    listar_productos,
    obtener_producto_por_id,
    obtener_tipo_config,
    obtener_tipos_producto,
    validar_formulario,
)


productos_bp = Blueprint("productos", __name__, url_prefix="/productos")


@productos_bp.route("/", methods=["GET"])
def listar_productos_view():
    tipo_producto = request.args.get("tipo", DEFAULT_PRODUCT_TYPE)
    tipos_producto = obtener_tipos_producto()
    config = obtener_tipo_config(tipo_producto)

    productos = []
    error_carga = None
    try:
        productos = listar_productos(tipo_producto)
    except Error as error:
        error_carga = (
            "No fue posible cargar los productos. "
            "Revisa la configuracion de MySQL y la existencia de las tablas."
        )

    return render_template(
        "productos/lista.html",
        productos=productos,
        tipo_producto=tipo_producto,
        tipos_producto=tipos_producto,
        config=config,
        error_carga=error_carga,
    )


@productos_bp.route("/nuevo", methods=["GET", "POST"])
def crear_producto_view():
    tipo_producto = request.args.get("tipo", DEFAULT_PRODUCT_TYPE)
    tipos_producto = obtener_tipos_producto()
    config = obtener_tipo_config(tipo_producto)
    form_data = _empty_form_data(config)

    if request.method == "POST":
        form_data = request.form.to_dict()
        errores = validar_formulario(tipo_producto, form_data)
        if errores:
            for error in errores:
                flash(error, "error")
        else:
            try:
                crear_producto(tipo_producto, form_data)
                flash("Producto creado correctamente.", "success")
                return redirect(url_for("productos.listar_productos_view", tipo=tipo_producto))
            except Error as error:
                if es_error_bd_duplicado(error):
                    flash("Ya existe un producto con ese codigo.", "error")
                else:
                    flash("No fue posible guardar el producto en la base de datos.", "error")

    return render_template(
        "productos/formulario.html",
        accion="Crear",
        config=config,
        tipo_producto=tipo_producto,
        tipos_producto=tipos_producto,
        form_data=form_data,
    )


@productos_bp.route("/<tipo_producto>/<int:producto_id>/editar", methods=["GET", "POST"])
def editar_producto_view(tipo_producto, producto_id):
    tipos_producto = obtener_tipos_producto()
    config = obtener_tipo_config(tipo_producto)

    try:
        producto = obtener_producto_por_id(tipo_producto, producto_id)
    except Error:
        flash("No fue posible cargar el producto.", "error")
        return redirect(url_for("productos.listar_productos_view", tipo=tipo_producto))

    if not producto:
        flash("Producto no encontrado.", "error")
        return redirect(url_for("productos.listar_productos_view", tipo=tipo_producto))

    form_data = _producto_to_form_data(config, producto)

    if request.method == "POST":
        form_data = request.form.to_dict()
        errores = validar_formulario(tipo_producto, form_data)
        if errores:
            for error in errores:
                flash(error, "error")
        else:
            try:
                actualizar_producto(tipo_producto, producto_id, form_data)
                flash("Producto actualizado correctamente.", "success")
                return redirect(url_for("productos.listar_productos_view", tipo=tipo_producto))
            except Error as error:
                if es_error_bd_duplicado(error):
                    flash("Ya existe un producto con ese codigo.", "error")
                else:
                    flash("No fue posible actualizar el producto.", "error")

    return render_template(
        "productos/formulario.html",
        accion="Editar",
        config=config,
        tipo_producto=tipo_producto,
        tipos_producto=tipos_producto,
        form_data=form_data,
    )


@productos_bp.route("/<tipo_producto>/<int:producto_id>/eliminar", methods=["POST"])
def eliminar_producto_view(tipo_producto, producto_id):
    try:
        eliminar_producto(tipo_producto, producto_id)
        flash("Producto eliminado correctamente.", "success")
    except Error:
        flash("No fue posible eliminar el producto.", "error")

    return redirect(url_for("productos.listar_productos_view", tipo=tipo_producto))


def _empty_form_data(config):
    form_data = {
        config["code_field"]: "",
        "nombre": "",
        config["price_field"]: "",
    }
    if config["has_quantity"]:
        form_data["cantidad"] = ""
    return form_data


def _producto_to_form_data(config, producto):
    form_data = {
        config["code_field"]: str(producto.get(config["code_field"], "")),
        "nombre": producto.get("nombre", ""),
        config["price_field"]: str(producto.get(config["price_field"], "")),
    }
    if config["has_quantity"]:
        form_data["cantidad"] = str(producto.get("cantidad", ""))
    return form_data
