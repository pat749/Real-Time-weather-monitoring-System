# src/alerting_system.py

from config.config import TEMP_THRESHOLD

def check_alerts(weather_data):
    alerts = []
    for city, data in weather_data.items():
        if data['temperature'] > TEMP_THRESHOLD:
            alerts.append(f"Alert: {city} temperature is above {TEMP_THRESHOLD}°C: {data['temperature']}°C")
    return alerts
