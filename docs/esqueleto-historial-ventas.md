# Esqueleto de Historial de Ventas

## Objetivo
Crear una pagina separada para consultar las ventas ya finalizadas.

## Funcion principal
- Ver ventas registradas
- Ver fecha y hora de cada venta
- Ver tipo de pago
- Ver total de cada venta
- Ver detalle de productos vendidos por cada venta

## Filtros minimos propuestos
- Fecha
- Tipo de pago

## Estructura de la pagina

### 1. Encabezado
- Titulo del modulo
- Resumen de cantidad de ventas encontradas
- Resumen de total acumulado mostrado

### 2. Zona de filtros
- Fecha exacta
- Tipo de pago: efectivo o tarjeta
- Boton para filtrar
- Boton para limpiar filtros

### 3. Lista de ventas
Cada venta debe mostrar:
- ID o numero de venta
- Fecha y hora
- Tipo de pago
- Total

### 4. Detalle por venta
Cada venta debe permitir ver:
- Codigo del producto
- Nombre
- Cantidad
- Unidad
- Precio de referencia
- Subtotal

## Uso esperado
1. El usuario entra a historial de ventas.
2. Aplica filtro si quiere revisar un dia o tipo de pago.
3. Consulta totales y detalle de cada venta.

## Sectores tecnicos a intervenir
- Servicio nuevo de lectura de historial
- Ruta nueva
- Plantilla nueva
- Navegacion base y landing
