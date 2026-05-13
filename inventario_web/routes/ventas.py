from decimal import Decimal

from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from mysql.connector import Error

from inventario_web.services.ventas_service import (
    agregar_producto_al_carrito,
    eliminar_item_del_carrito,
    finalizar_venta,
    obtener_carrito_vacio,
    obtener_total_carrito,
    preparar_producto_para_venta,
)


ventas_bp = Blueprint("ventas", __name__, url_prefix="/ventas")


@ventas_bp.route("/", methods=["GET"])
def venta_view():
    carrito = _obtener_carrito()
    total = obtener_total_carrito(carrito)
    return render_template(
        "ventas/venta.html",
        carrito=carrito,
        producto_preparado=None,
        total=total,
    )


@ventas_bp.route("/preparar", methods=["POST"])
def preparar_producto_venta_view():
    carrito = _obtener_carrito()
    total = obtener_total_carrito(carrito)
    codigo = request.form.get("codigo", "")

    try:
        producto_preparado, error = preparar_producto_para_venta(codigo)
    except Error:
        flash("No fue posible buscar el producto en la base de datos.", "error")
        return redirect(url_for("ventas.venta_view"))

    if error:
        flash(error, "error")
        return redirect(url_for("ventas.venta_view"))

    return render_template(
        "ventas/venta.html",
        carrito=carrito,
        producto_preparado=producto_preparado,
        total=total,
    )


@ventas_bp.route("/agregar", methods=["POST"])
def agregar_producto_venta_view():
    carrito = _obtener_carrito()
    codigo = request.form.get("codigo", "")
    cantidad = request.form.get("cantidad", "")

    try:
        carrito_actualizado, error = agregar_producto_al_carrito(carrito, codigo, cantidad)
    except Error:
        flash("No fue posible buscar el producto en la base de datos.", "error")
        return redirect(url_for("ventas.venta_view"))

    if error:
        flash(error, "error")
        return redirect(url_for("ventas.venta_view"))

    session["venta_carrito"] = carrito_actualizado
    flash("Producto agregado a la venta.", "success")
    return redirect(url_for("ventas.venta_view"))


@ventas_bp.route("/eliminar/<int:item_index>", methods=["POST"])
def eliminar_item_venta_view(item_index):
    carrito = _obtener_carrito()
    session["venta_carrito"] = eliminar_item_del_carrito(carrito, item_index)
    flash("Linea eliminada de la venta.", "success")
    return redirect(url_for("ventas.venta_view"))


@ventas_bp.route("/vaciar", methods=["POST"])
def vaciar_venta_view():
    session["venta_carrito"] = obtener_carrito_vacio()
    flash("Venta vaciada correctamente.", "success")
    return redirect(url_for("ventas.venta_view"))


@ventas_bp.route("/finalizar", methods=["POST"])
def finalizar_venta_view():
    carrito = _obtener_carrito()
    total = obtener_total_carrito(carrito)

    try:
        error = finalizar_venta(carrito)
    except Error:
        flash("No fue posible finalizar la venta.", "error")
        return redirect(url_for("ventas.venta_view"))

    if error:
        flash(error, "error")
        return redirect(url_for("ventas.venta_view"))

    session["venta_carrito"] = obtener_carrito_vacio()
    flash(f"Venta finalizada. Total calculado: ${_formatear_total(total)}.", "success")
    return redirect(url_for("ventas.venta_view"))


def _obtener_carrito():
    return session.get("venta_carrito", obtener_carrito_vacio())


def _formatear_total(total):
    return format(Decimal(total), ".2f")
