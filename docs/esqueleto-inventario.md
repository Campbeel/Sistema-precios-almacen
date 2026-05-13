# Esqueleto de Inventario

## Objetivo
Definir la estructura inicial del inventario para productos con codigo de barra, productos sin codigo propio y productos a granel.

## Alcance de este modulo
- Registrar productos con codigo de barra
- Registrar productos sin codigo de barra usando codigo interno
- Registrar productos a granel usando codigo interno
- Consultar nombre, precio y cantidad segun tipo de producto

## Estructura propuesta

### 1. Productos con codigo de barra
Uso: productos que ya traen un codigo identificable desde fabrica o proveedor.

Campos base:
- `codigo_barra`
- `nombre`
- `precio`
- `cantidad`

### 2. Productos sin codigo de barra
Uso: productos que no tienen codigo propio y se venden por unidad.

Campos base:
- `codigo_interno`
- `nombre`
- `precio`
- `cantidad`

Ejemplos:
- `01` -> Ensalada
- `05` -> Pan amasado unidad

### 3. Productos a granel
Uso: productos vendidos por peso.

Campos base:
- `codigo_interno`
- `nombre`
- `precio_kilo`

Ejemplos:
- `01` -> Kilo de pan
- `05` -> Queso granel

## Reglas base
- `codigo_barra` debe ser unico
- `codigo_interno` debe ser unico dentro de su tabla
- Los codigos internos deben guardarse como texto para conservar formatos como `01`, `05` o `001`
- Los precios deben guardarse en formato decimal
- La cantidad de productos por unidad debe guardarse como numero entero

## Recomendaciones tecnicas
- Agregar un `id` interno en cada tabla aunque el usuario no lo vea
- Agregar campo `activo` para deshabilitar productos sin borrarlos
- Agregar fechas de creacion y actualizacion para control interno

## Punto pendiente a confirmar
- En productos a granel, por ahora se deja la tabla con `nombre` y `precio_kilo` como pediste.
- Si despues quieres controlar stock real a granel, convendra agregar un campo como `cantidad_kilos`.

## Flujo de uso esperado
1. El usuario registra el producto en la tabla que corresponda.
2. El sistema guarda precio y cantidad segun el tipo de producto.
3. La consulta de venta busca por codigo de barra o por codigo interno.
4. El inventario se actualiza segun las ventas o ajustes manuales.
