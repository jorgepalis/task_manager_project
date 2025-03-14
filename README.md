# Task Manager Project

Este proyecto es un sistema de gestión de tareas desarrollado con Django. Permite a los usuarios crear, editar, eliminar y visualizar tareas, así como marcar tareas como completadas. Además, incluye la funcionalidad de mostrar el clima actual de la ciudad asociada a cada tarea.

## Requisitos

- Python 3.x
- Django
- Django REST Framework

## Instalación

1. Clona el repositorio:
   ```
   git clone https://github.com/jorgepalis/task_manager_project.git
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

## Tests

El proyecto incluye una serie de tests para asegurar la calidad y el correcto funcionamiento de las diferentes funcionalidades:

### Tests de Modelos y Formularios
- **Creación de tareas**: Verifica que una tarea no pueda ser creada con un título vacío.
- **Validación de datos**: Comprueba que los campos obligatorios estén presentes y con el formato correcto.

### Tests de Funcionalidades
- **Cambio de estado "completed"**: Verifica que una tarea pueda ser marcada como completada correctamente.
- **Filtrado de tareas**: Asegura que el filtrado por estado funciona según lo esperado.

### Tests de Integración con API Externa
- **Consumo de API del clima**: Utiliza `unittest.mock` para simular respuestas de la API externa y verificar el correcto procesamiento de los datos del clima.
- **Manejo de errores**: Comprueba que la aplicación maneja adecuadamente los casos de error en la API externa.

### Ejecución de Tests

Para ejecutar todos los tests del proyecto:
```
python manage.py test task_manager
```
Para ejecutar un test específico:
```
python manage.py test task_manager.tests.TaskModelTest
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.