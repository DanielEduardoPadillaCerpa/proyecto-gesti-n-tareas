# Gestor de Tareas con Tkinter y SQLAlchemy

Este proyecto es una aplicación de escritorio para la gestión de tareas, desarrollada en Python utilizando las bibliotecas Tkinter para la interfaz gráfica y SQLAlchemy para la gestión de bases de datos. La aplicación permite crear, listar, completar, eliminar y guardar tareas en un archivo JSON.

## Características

- **Inicio de sesión**: Pantalla de inicio de sesión con credenciales predefinidas.
- **Gestor de tareas**:
  - Agregar nuevas tareas con título y descripción.
  - Marcar tareas como completadas.
  - Eliminar tareas.
  - Guardar tareas en un archivo JSON.
  - Cargar tareas desde un archivo JSON.
  - Listar todas las tareas en una tabla interactiva.
- **Base de datos**: Almacenamiento persistente de las tareas utilizando SQLite.

## Requisitos previos

Asegúrese de tener instalados los siguientes requisitos:

- Python 3.8 o superior.
- Bibliotecas requeridas:
  - `tkinter` (incluido en la instalación estándar de Python).
  - `sqlalchemy`

Puedes instalar SQLAlchemy ejecutando:

```bash
pip install sqlalchemy
```

## Configuración del entorno

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener las dependencias instaladas.
3. Ejecuta el archivo principal `main.py` para iniciar la aplicación.

## Uso

### Inicio de sesión
Al abrir la aplicación, se te presentará una pantalla de inicio de sesión. Ingresa las siguientes credenciales para acceder:

- **Usuario**: `Daniel`
- **Contraseña**: `12345`

### Gestor de tareas

Una vez iniciada sesión, accedes al gestor de tareas donde puedes:

1. **Agregar una tarea**:
   - Completa los campos de "Título" y "Descripción" y haz clic en "Agregar Tarea".

2. **Listar tareas**:
   - Haz clic en "Listar Tareas" para ver todas las tareas almacenadas en la base de datos.

3. **Completar una tarea**:
   - Selecciona una tarea en la tabla y haz clic en "Completar Tarea" para marcarla como completada.

4. **Eliminar una tarea**:
   - Selecciona una tarea en la tabla y haz clic en "Eliminar Tarea".

5. **Guardar tareas**:
   - Haz clic en "Guardar Tareas" para exportar las tareas a un archivo JSON.

6. **Cargar tareas**:
   - Haz clic en "Cargar Tareas" para importar tareas desde un archivo JSON.

### Datos adicionales

Las tareas se almacenan en una base de datos SQLite (`gestion_tareas.db`) utilizando el modelo `Tarea` definido en SQLAlchemy. Las tareas también pueden ser exportadas e importadas en formato JSON.

## Estructura del código

- **Base de datos**:
  - Archivo SQLite configurado con SQLAlchemy.
  - Modelo `Tarea` con los campos: `id`, `titulo`, `descripcion` y `completada`.

- **Interfaz gráfica**:
  - Ventana de inicio de sesión (clase `LoginWindow`).
  - Ventana principal para la gestión de tareas (clase `TaskApp`).
  
- **Funciones principales**:
  - Agregar, listar, completar y eliminar tareas.
  - Guardar y cargar tareas desde un archivo JSON.

## Capturas de pantalla

### Inicio de sesión
![Captura de pantalla 2024-12-15 200410](https://github.com/user-attachments/assets/3ab2cdbd-7adf-4b55-8502-750095a64c6d)

### Gestor de tareas
![imagen_2024-12-15_200640023](https://github.com/user-attachments/assets/877d2eac-1faf-4bcb-99ac-47a7cd157f9f)



## Tecnologías utilizadas

- **Lenguaje**: Python 3.
- **Bibliotecas**:
  - Tkinter: Diseño de la interfaz gráfica.
  - SQLAlchemy: ORM para la gestión de la base de datos SQLite.
  - JSON: Exportación e importación de tareas.

## Mejoras futuras

1. Implementar un sistema de usuarios múltiples con almacenamiento de credenciales en la base de datos.
2. Agregar una funcionalidad para categorizar tareas.
3. Diseñar un sistema de notificación para recordar tareas pendientes.
4. Mejorar la estética de la interfaz con una biblioteca como `ttkbootstrap` o `customtkinter`.
5. Internacionalización del sistema para soportar varios idiomas.

## Autor

Este proyecto fue desarrollado como por Daniel Eduardo Padilla Cerpa y puede ser modificado según las necesidades del usuario.
