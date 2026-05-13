USE almacen_interno;

CREATE TABLE IF NOT EXISTS ventas_historial (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_pago ENUM('efectivo', 'tarjeta') NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    fecha_venta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ventas_historial_detalle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    venta_id INT NOT NULL,
    tipo_producto VARCHAR(30) NOT NULL,
    producto_id INT NOT NULL,
    codigo_producto VARCHAR(50) NOT NULL,
    nombre_producto VARCHAR(150) NOT NULL,
    cantidad DECIMAL(10,2) NOT NULL,
    unidad_medida VARCHAR(20) NOT NULL,
    precio_referencia DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (venta_id) REFERENCES ventas_historial(id)
);
