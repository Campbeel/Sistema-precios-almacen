# Esqueleto de Navegacion y Venta

## Objetivo
Agregar una pagina principal de entrada y separar el sistema en tres accesos claros:
- mantenimiento de inventario
- consulta total de inventario
- venta interna

## Flujo general propuesto
1. El usuario entra a la aplicacion.
2. Ve una landing con las opciones principales.
3. Desde la landing puede entrar a:
   - CRUD de inventario
   - lista total de inventario
   - venta

## Modulo 1: Landing

### Funcion
- Servir como pagina inicial de entrada
- Mostrar accesos rapidos a cada area del sistema

### Opciones visibles
- Inventario: ingresar, editar o eliminar productos
- Inventario total: ver productos y cantidades disponibles
- Venta: cargar productos por codigo y ver total

## Modulo 2: Inventario total

### Funcion
- Mostrar el inventario completo para consulta

### Estructura propuesta
- Seccion de productos con codigo de barra
- Seccion de productos sin codigo
- Seccion de productos a granel

### Datos visibles
- Codigo
- Nombre
- Precio o precio por kilo
- Cantidad si aplica

### Nota
- Productos a granel no tienen por ahora stock en kilos, por lo que se mostraran sin cantidad controlada

## Modulo 3: Venta

### Funcion
- Permitir agregar productos a una venta usando codigo ingresado manualmente o lector de codigo de barras

### Flujo base
1. El usuario ingresa un codigo.
2. El sistema busca primero en productos con codigo de barra.
3. Si no encuentra, busca en productos sin codigo y granel por codigo interno.
4. Si encuentra el producto, detecta si se vende por unidad o por peso.
5. Si es por unidad, solicita cantidad en unidades.
6. Si es granel, solicita peso en gramos.
7. Luego agrega el producto al detalle de venta.
8. El sistema muestra lineas agregadas y total acumulado.
9. El usuario finaliza la venta.

### Reglas base
- Productos por unidad usan cantidad entera
- Productos a granel se ingresan en gramos
- Si el producto por unidad no tiene stock suficiente, no se agrega
- Al finalizar la venta, se descuenta stock solo en productos con cantidad controlada
- El pago ocurre por un sistema externo, por lo que aqui solo se calcula y confirma el total

## Sectores tecnicos a intervenir
- Rutas nuevas para landing, inventario total y venta
- Servicios nuevos de consulta general y venta
- Plantillas HTML nuevas
- Ajuste menor de navegacion base

## Pendiente futuro
- Guardar historial de ventas
- Registrar medio de pago externo como referencia
- Manejar stock en kilos para granel
