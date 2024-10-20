# src/data_storage.py

import sqlite3
from config.config import CITIES

def create_table():
    conn = sqlite3.connect('data/weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temperature REAL,
            condition TEXT,
            humidity REAL,
            wind_speed REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_weather_data(weather_data):
    conn = sqlite3.connect('data/weather.db')
    cursor = conn.cursor()
    for city, data in weather_data.items():
        cursor.execute('''
            INSERT INTO weather (city, temperature, condition, humidity, wind_speed) 
            VALUES (?, ?, ?, ?, ?)
        ''', (city, data['temperature'], data['condition'], data['humidity'], data['wind_speed']))
    conn.commit()
    conn.close()
