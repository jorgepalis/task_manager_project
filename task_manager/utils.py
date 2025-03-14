import os
from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework.decorators import api_view, renderer_classes

# Cargar variables de entorno
load_dotenv()
key = os.getenv('WEATHER_API_KEY')

# Usando DRF para consumir la API externa
@api_view(['GET'])
def get_weather_api(request, city):
    """Vista API para obtener datos del clima usando DRF"""
    from rest_framework import serializers
    import requests
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=sp&appid={key}&units=metric"
    
    try:
        # Consumir la API externa
        response = requests.get(url)
        weather_data = response.json()
        
        # Procesar respuesta
        if response.status_code == 200:
            return JsonResponse({
                'success': True,
                'temperatura': f"{weather_data['main']['temp']} °C",
                'descripcion': weather_data['weather'][0]['description'],
                'humedad': f"{weather_data['main']['humidity']} %"
            })
        elif response.status_code == 404:
            return JsonResponse({
                'success': False,
                'error': "No se encontró la ciudad"
            }, status=404)
        else:
            return JsonResponse({
                'success': False,
                'error': "Error en el servicio"
            }, status=response.status_code)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': f"Error al conectar con el servicio: {str(e)}"
        }, status=500)

# Mantener la función existente para compatibilidad
def get_weather(city):
    """Función para obtener datos del clima"""
    import requests
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=sp&appid={key}&units=metric"
    
    try:
        response = requests.get(url).json()

        if response.get("main"):
            temperatura = response['main']['temp']
            descripcion = response['weather'][0]['description']
            humedad = response['main']['humidity']
            data = {
                'success': True,
                'temperatura': f"{temperatura} °C",
                'descripcion': descripcion,
                'humedad': f"{humedad} %"
            }
            return data

        if response.get('cod') == '404':
            data = {
                'success': False,
                'error': "No se encontró la ciudad"
            }
            return data
        else:
            data = {
                'success': False,
                'error': "Error en el servicio"
            }
            return data
    except Exception as e:
        return {
            'success': False,
            'error': f"Error de conexión: {str(e)}"
        }

