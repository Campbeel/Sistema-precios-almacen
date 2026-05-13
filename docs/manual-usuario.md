# Manual de Usuario

## Objetivo
Explicar el uso de la aplicacion del almacen de forma simple y ordenada.

## Estado del manual
- Version del manual: 0.1
- Estado: Base inicial
- Publico objetivo: Usuario operador del almacen

## Acceso al sistema
- URL o ruta local:
- Usuario:
- Clave:
- Observaciones:

## Modulos principales

### 0. Landing principal
- Objetivo: Dar acceso rapido a las areas principales del sistema.
- Pasos de uso:
  1. Ingresar a la aplicacion.
  2. Elegir entre inventario, inventario total o venta.
  3. Entrar al modulo que corresponda a la tarea del momento.
- Resultado esperado: El usuario entra al area correcta sin pasar directo al CRUD.

### 1. Consulta de productos
- Objetivo:
- Pasos de uso:
  1. 
  2. 
  3. 
- Resultado esperado:

### 2. Lector de codigo de barras
- Objetivo:
- Requisitos previos:
- Pasos de uso:
  1. 
  2. 
  3. 
- Resultado esperado:
- Problemas comunes:

### 3. Gestion de inventario
- Objetivo: Registrar y consultar productos segun su tipo dentro del almacen
- Pasos de uso:
  1. Registrar productos con codigo de barra en su tabla correspondiente.
  2. Registrar productos sin codigo propio usando codigo interno.
  3. Registrar productos a granel con su nombre y precio por kilo.
- Resultado esperado: El sistema diferencia correctamente cada tipo de producto para consulta y control interno.

### 6. CRUD de productos
- Objetivo: Crear, visualizar, editar y eliminar productos desde la interfaz del sistema.
- Pasos de uso:
  1. Ingresar al modulo de productos.
  2. Elegir el tipo de producto: con codigo de barra, sin codigo o granel.
  3. Crear o editar el producto llenando el formulario correspondiente.
  4. Eliminar un producto solo si ya no debe existir en el registro.
- Resultado esperado: El producto queda guardado y visible en la lista del tipo seleccionado.

### 7. Inventario total
- Objetivo: Ver el stock y precios cargados en todo el sistema.
- Pasos de uso:
  1. Ingresar a la landing principal.
  2. Abrir la opcion inventario total.
  3. Revisar cada bloque: con codigo de barra, sin codigo y granel.
- Resultado esperado: El usuario puede consultar rapidamente lo disponible en cada categoria.

### 8. Venta
- Objetivo: Cargar productos por codigo y calcular el total de una venta.
- Pasos de uso:
  1. Ingresar a la landing principal.
  2. Abrir la opcion venta.
  3. Ingresar el codigo del producto.
  4. Verificar el codigo para que el sistema identifique el tipo de producto.
  5. Si es producto unitario, ingresar cantidad en unidades.
  6. Si es producto a granel, ingresar el peso en gramos.
  7. Agregar productos hasta completar la venta.
  8. Seleccionar tipo de pago: efectivo o tarjeta.
  9. Finalizar la venta para descontar stock en productos con cantidad controlada.
- Resultado esperado: El sistema muestra el detalle de la venta, el total calculado y guarda la venta en el historial.

Nota operativa:
Las cantidades unitarias se ingresan como numeros enteros. Los productos a granel se ingresan en gramos enteros. Los montos se trabajan en CLP aproximados a decenas.

### 9. Historial de ventas
- Objetivo: Revisar ventas ya registradas en el sistema.
- Pasos de uso:
  1. Ingresar a la landing principal o barra superior.
  2. Abrir la opcion historial.
  3. Filtrar por fecha y/o tipo de pago si es necesario.
  4. Revisar el total de cada venta y su detalle de productos.
- Resultado esperado: El usuario puede consultar ventas pasadas por dia y revisar su contenido.

### 4. Actualizacion de precios
- Objetivo:
- Pasos de uso:
  1. 
  2. 
  3. 
- Resultado esperado:

### 5. Productos sin codigo de barra
- Objetivo:
- Pasos de uso:
  1. 
  2. 
  3. 
- Resultado esperado:

## Mensajes de error y apoyo

### Error o situacion
- Descripcion:
- Causa posible:
- Solucion:

## Buenas practicas de uso
- Verificar que el lector este conectado antes de iniciar
- Confirmar el producto antes de actualizar precio o stock
- Registrar cambios relevantes si el sistema incorpora trazabilidad

## Historial del manual

| Fecha | Cambio | Observaciones |
| --- | --- | --- |
| 2026-05-12 | Se crea estructura inicial del manual de usuario | Base para documentar el uso real de la aplicacion |
| 2026-05-12 | Se agrega base descriptiva del modulo de inventario | Incluye tipos de productos contemplados en la primera etapa |
| 2026-05-12 | Se agrega descripcion inicial del CRUD de productos | Base para la operacion del backend web |
| 2026-05-13 | Se agregan modulos de landing, inventario total y venta | Manual inicial de navegacion y uso operativo |
| 2026-05-13 | Se agrega cierre de venta con tipo de pago e historial | La venta ya registra informacion persistente |
| 2026-05-13 | Se agrega pagina de historial de ventas | Incluye filtros y detalle por venta |
