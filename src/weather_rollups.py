# src/weather_rollups.py

def calculate_rollups(weather_data):
    total_temp = 0
    max_temp = float('-inf')
    min_temp = float('inf')
    condition_count = {}

    for city, data in weather_data.items():
        total_temp += data['temperature']
        max_temp = max(max_temp, data['temperature'])
        min_temp = min(min_temp, data['temperature'])
        
        condition_count[data['condition']] = condition_count.get(data['condition'], 0) + 1

    average_temp = total_temp / len(weather_data)
    dominant_condition = max(condition_count, key=condition_count.get)

    return {
        'average_temp': average_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition
    }
