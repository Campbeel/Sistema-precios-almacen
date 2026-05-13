CREATE USER IF NOT EXISTS 'almacen_app'@'localhost' IDENTIFIED BY 'Pama5121';
ALTER USER 'almacen_app'@'localhost' IDENTIFIED BY 'Pama5121';
GRANT ALL PRIVILEGES ON almacen_interno.* TO 'almacen_app'@'localhost';
FLUSH PRIVILEGES;
