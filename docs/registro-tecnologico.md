# Registro Tecnologico

## Objetivo
Documentar cada tecnologia usada, decisiones tecnicas tomadas y cambios incorporados al sistema del almacen.

## Estado del proyecto
- Nombre: Sistema de precios e inventario para almacen
- Estado actual: En definicion inicial
- Alcance base:
  - Inventario de productos
  - Lector de codigos de barra
  - Consulta y actualizacion de precios
  - Interfaz para productos sin codigo de barra
  - Uso interno para apoyo de venta y orden operativo
  - No orientado a ecommerce ni venta publica en internet

## Tecnologias activas
Stack base definido para la primera etapa del proyecto.

### Backend
- Lenguaje: Python
- Framework: Flask
- Version: Python 3
- Observaciones: Backend principal del sistema para logica de negocio, inventario, ventas internas e integracion con lector si corresponde

### Base de datos
- Motor: MySQL
- Tipo de instalacion: Por definir entre local o servidor
- Version: Por definir
- Observaciones: Base principal para productos, precios e inventario

### Frontend
- Lenguaje: HTML
- Framework o libreria: HTML + CSS + JavaScript basico
- Version: HTML5
- Observaciones: Base para formularios, vistas de productos y flujo de consulta en entorno interno

### Integraciones
- Lector de codigos:
- Libreria o SDK:
- Observaciones:

### Dependencias Python
- Flask
- mysql-connector-python

## Decisiones tecnicas
Registrar aqui decisiones importantes y el motivo.

### Decision 001
- Fecha: 2026-05-12
- Tema: Stack tecnologico inicial
- Decision: Usar Python 3, MySQL y HTML como base del sistema; CSS y JavaScript se consideran apoyo normal de interfaz
- Motivo: Cubrir logica de negocio, base de datos relacional e interfaz interna con tecnologias conocidas y adecuadas para uso propio
- Impacto: Se simplifica la arquitectura al evitar dos backends en paralelo

### Decision 002
- Fecha: 2026-05-12
- Tema: Documentacion tecnica
- Decision: Registrar cada tecnologia y cambio en este archivo
- Motivo: Mantener trazabilidad tecnica ordenada
- Impacto: Cada nueva dependencia o modulo debe quedar asentado aqui

### Decision 003
- Fecha: 2026-05-12
- Tema: Alcance del sistema
- Decision: El sistema sera de uso interno, enfocado en orden, inventario y apoyo de venta en almacen
- Motivo: Resolver dificultad operativa por alto volumen de productos, sin necesidades de ecommerce
- Impacto: Se prioriza simplicidad, operacion local y rapidez de uso sobre escalabilidad publica

### Decision 004
- Fecha: 2026-05-12
- Tema: Backend principal
- Decision: Python sera el backend principal del sistema
- Motivo: Es la tecnologia con la que el desarrollo tendra mayor continuidad de aprendizaje y productividad
- Impacto: PHP queda fuera del stack base salvo que aparezca una necesidad concreta mas adelante

### Decision 005
- Fecha: 2026-05-12
- Tema: Estructura inicial de inventario
- Decision: Separar inventario en tres tablas: productos con codigo de barra, productos sin codigo propio y productos a granel
- Motivo: Reflejar con claridad los tipos reales de producto que maneja el almacen
- Impacto: La consulta y mantencion del inventario sera mas simple en una primera etapa

### Decision 006
- Fecha: 2026-05-12
- Tema: Codigos internos
- Decision: Los codigos internos se guardaran como texto
- Motivo: Permitir formatos como `01`, `05` o `001` sin perder ceros a la izquierda
- Impacto: Las busquedas y registros internos deben tratar estos codigos como cadenas

### Decision 007
- Fecha: 2026-05-12
- Tema: Base del CRUD web
- Decision: Implementar el primer CRUD de productos usando Flask y plantillas HTML
- Motivo: Permitir una base visible, simple y rapida de modificar para el sistema interno
- Impacto: Se agrega una estructura inicial de backend web y vistas para crear, listar, editar y eliminar productos

### Decision 008
- Fecha: 2026-05-12
- Tema: Control de archivos en Git
- Decision: Agregar un `.gitignore` para excluir archivos locales y autogenerados
- Motivo: Evitar subir a GitHub entornos virtuales, variables locales, caches y archivos temporales
- Impacto: El repositorio queda mas limpio y seguro para trabajo compartido

### Decision 009
- Fecha: 2026-05-12
- Tema: Acceso de la aplicacion a MySQL
- Decision: Crear un usuario dedicado `almacen_app` para la aplicacion
- Motivo: Evitar usar `root` desde Flask y separar acceso administrativo de acceso de la app
- Impacto: La conexion del backend debe configurarse con este usuario en el archivo de entorno

### Decision 010
- Fecha: 2026-05-12
- Tema: Carga de configuracion local
- Decision: Leer variables desde un archivo `.env` local al iniciar la aplicacion
- Motivo: Simplificar la configuracion del backend en entorno local sin depender de exportar variables manualmente
- Impacto: La app puede arrancar con `python app.py` usando la configuracion local del proyecto

## Bitacora de cambios
Registrar cada cambio tecnico con fecha y alcance.

| Fecha | Modulo/Sector | Cambio realizado | Tecnologia involucrada | Observaciones |
| --- | --- | --- | --- | --- |
| 2026-05-12 | Documentacion | Se crea estructura inicial de registro tecnico, manual de usuario y plantilla de trabajo | Markdown | Base para trabajo controlado |
| 2026-05-12 | Arquitectura base | Se registra stack base definido: Python 3, MySQL, HTML, CSS y JavaScript basico | Python 3, MySQL, HTML5, CSS, JavaScript | Python queda como backend principal |
| 2026-05-12 | Alcance funcional | Se define que el sistema es de uso interno y no ecommerce | Arquitectura | Esto reduce necesidades de despliegue y complejidad |
| 2026-05-12 | Inventario | Se crea esqueleto funcional del inventario y script MySQL inicial para tres tablas | MySQL, Markdown | Se deja separado del archivo sqlproj existente |
| 2026-05-12 | Backend productos | Se crea base CRUD web para productos sobre Flask y MySQL | Python, Flask, MySQL, HTML, CSS | Incluye listar, crear, editar y eliminar por tipo de producto |
| 2026-05-12 | Control de versiones | Se agrega `.gitignore` para excluir archivos locales del entorno de trabajo | Git | Se ignoran `.venv`, `.env`, caches y logs |
| 2026-05-12 | Base de datos | Se agrega script para crear usuario de aplicacion en MySQL | MySQL | Permite conectar Flask sin usar root |
| 2026-05-12 | Configuracion local | Se agrega carga de `.env` y archivo local base para conexion del backend | Python, configuracion | La clave real debe reemplazarse manualmente |

## Pendientes tecnicos
- Definir base de datos local o en servidor
- Definir metodo de integracion del lector de codigos de barra
- Definir estrategia de despliegue: local o AWS
- Confirmar si productos a granel manejaran tambien stock en kilos

## Tecnologias posiblemente necesarias

### CSS
- Motivo: Necesario para dar estructura visual utilizable a formularios, botones y pantallas

### JavaScript
- Motivo: Conveniente para validaciones en pantalla, lectura rapida de formularios y mejor respuesta de interfaz

### Conector MySQL
- Opcion en Python: `mysql-connector-python` o equivalente
- Motivo: Necesario para conectar la aplicacion con MySQL

### Flask
- Motivo: Necesario para construir rutas, formularios y vistas web del CRUD interno

## Observaciones del repositorio actual
- El archivo `San-Sebastian.sqlproj` corresponde a un proyecto de SQL Server
- Para evitar mezclar motores, el esquema inicial de inventario en esta etapa se deja en un script nuevo orientado a MySQL

## Evaluacion de infraestructura

### Opcion A: Funcionamiento local
- Ventajas: Menor costo, mayor simplicidad, facil control operativo, suficiente para uso interno
- Desventajas: Dependencia del equipo local y respaldo manual si no se automatiza
- Requisitos: PC estable, red local si habra mas de un equipo, plan de copias de seguridad

### Opcion B: Servidor AWS
- Ventajas: Acceso remoto, respaldo y continuidad mas faciles de ampliar
- Desventajas: Mayor complejidad y costo innecesario para una primera etapa interna
- Requisitos: Definir seguridad, despliegue, monitoreo y costos operativos

### Decision pendiente
- Opcion elegida:
- Motivo:
- Fecha:
