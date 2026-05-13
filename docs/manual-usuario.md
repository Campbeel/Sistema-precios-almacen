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
