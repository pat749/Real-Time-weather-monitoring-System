# src/visualization.py

import matplotlib.pyplot as plt
import sqlite3

def visualize_weather_data():
    conn = sqlite3.connect('data/weather.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT city, AVG(temperature) FROM weather GROUP BY city")
    data = cursor.fetchall()

    cities = [row[0] for row in data]
    avg_temps = [row[1] for row in data]

    plt.bar(cities, avg_temps)
    plt.xlabel('Cities')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Average Temperature in Indian Metros')
    plt.show()
    
    conn.close()
