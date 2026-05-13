USE almacen_interno;

ALTER TABLE ventas_historial
    MODIFY total INT NOT NULL;

ALTER TABLE ventas_historial_detalle
    MODIFY cantidad INT NOT NULL,
    MODIFY precio_referencia INT NOT NULL,
    MODIFY subtotal INT NOT NULL;
