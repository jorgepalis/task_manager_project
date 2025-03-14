import requests
import os
from dotenv import load_dotenv

# cargar variables de entorno
load_dotenv()

# obtener la clave de la api
key = os.getenv('WEATHER_API_KEY')

# funcion para obtener detaller del clima

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=sp&appid={key}&units=metric"
    response = requests.get(url).json()

    if response.get("main"):
        temperatura = response['main']['temp']
        descripcion = response['weather'][0]['description']
        humedad = response['main']['humidity']
        data = {
            'success': True,
            'temperatura': str(temperatura)+" "+'°C',
            'descripcion': descripcion,
            'humedad': str(humedad)+" "+'%'
        }
        return data

    if response['cod'] == '404':
        data = {
            'success': False,
            'error': "No se encontró la ciudad"       }
        return data
    else:
        data = {
            'success': False,
            'error': "Error en el servicio"
        }
        return data
    
