# Task Manager Project

Este proyecto es un sistema de gestión de tareas desarrollado con Django. Permite a los usuarios crear, editar, eliminar y visualizar tareas, así como marcar tareas como completadas. Además, incluye la funcionalidad de mostrar el clima actual de la ciudad asociada a cada tarea.

## Requisitos

- Python 3.x
- Django
- Django REST Framework

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd task_manager_project
   ```

2. Crea un entorno virtual y actívalo:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Realiza las migraciones de la base de datos:
   ```
   python manage.py migrate
   ```

5. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

## Estructura del Proyecto

- `manage.py`: Script de gestión del proyecto.
- `requirements.txt`: Lista de dependencias del proyecto.
- `.gitignore`: Archivos y directorios que deben ser ignorados por Git.
- `task_manager_project/`: Configuración del proyecto Django.
- `task_manager/`: Aplicación principal para la gestión de tareas.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.