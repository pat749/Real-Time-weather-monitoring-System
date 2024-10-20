# src/weather_fetcher.py

import requests
import logging
from config.config import API_KEY, CITIES

logging.basicConfig(level=logging.INFO)

def fetch_weather_data(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching weather data for {city}: {e}")
        return None

def fetch_all_weather_data():
    weather_data = {}
    for city in CITIES:
        data = fetch_weather_data(city)
        if data:
            weather_data[city] = {
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
    return weather_data
