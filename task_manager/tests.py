from django.test import TestCase, Client
from django.urls import reverse
from unittest import mock
from .models import Task
from .forms import TaskForm
from .utils import get_weather

class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            completed=False,
            due_date='2023-12-31',
            city='Test City'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task.')
        self.assertFalse(self.task.completed)
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_completed(self):
        self.task.completed = True
        self.task.save()
        self.assertTrue(self.task.completed)

    def test_task_due_date(self):
        # Corregir para manejar due_date como string
        self.assertEqual(self.task.due_date, '2023-12-31')

    def test_task_city(self):
        self.assertEqual(self.task.city, 'Test City')

class TaskTests(TestCase):
    def test_task_creation_empty_title(self):
        """Test que verifica que no se puede crear una tarea con título vacío"""
        # Usando el formulario directamente
        form = TaskForm(data={'title': '', 'description': 'Test description'})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        
        # Verificar cantidad de tareas en la base de datos
        self.assertEqual(Task.objects.count(), 0)
    
    def test_mark_task_completed(self):
        """Test que verifica el cambio de estado completed de una tarea"""
        # Crear una tarea de prueba
        task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            completed=False
        )
        
        # Verificar estado inicial
        self.assertFalse(task.completed)
        
        # Usar la vista para marcar como completada
        client = Client()
        response = client.post(
            reverse('task_manager:mark_task_completed', args=[task.id])
        )
        
        # Recargar la tarea desde la base de datos
        task.refresh_from_db()
        
        # Verificar que ahora está marcada como completada
        self.assertTrue(task.completed)

class WeatherAPITests(TestCase):
    @mock.patch('task_manager.utils.requests.get')
    def test_weather_api_success(self, mock_get):
        """Test que simula una respuesta exitosa de la API del clima"""
        # Configurar el mock para simular una respuesta exitosa
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'main': {
                'temp': 20.5,
                'humidity': 70
            },
            'weather': [
                {
                    'description': 'cielo despejado'
                }
            ]
        }
        mock_get.return_value = mock_response
        
        # Llamar a la función que obtiene el clima
        result = get_weather('Madrid')
        
        # Verificar con los formatos correctos que devuelve tu función
        self.assertTrue(result['success'])
        self.assertEqual(result['temperatura'], '20.5 °C')
        self.assertEqual(result['descripcion'], 'cielo despejado')
        self.assertEqual(result['humedad'], '70 %')

    @mock.patch('task_manager.utils.requests.get')
    def test_weather_api_error(self, mock_get):
        """Test que simula un error en la API del clima"""
        # Configurar mock para simular respuesta de ciudad no encontrada
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            'cod': '404',
            'message': 'city not found'
        }
        mock_get.return_value = mock_response
        
        # Llamar a la función que obtiene el clima
        result = get_weather('CiudadInexistente')
        
        # Verificar que la función maneja correctamente el error
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "No se encontró la ciudad")

    @mock.patch('task_manager.utils.requests.get')
    def test_weather_api_service_error(self, mock_get):
        """Test que simula un error genérico en el servicio de clima"""
        # Configurar mock para simular error de servicio
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            'cod': '500',
            'message': 'Internal server error'
        }
        mock_get.return_value = mock_response
        
        # Llamar a la función que obtiene el clima
        result = get_weather('Madrid')
        
        # Verificar que la función maneja correctamente el error
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], "Error en el servicio")