# src/main.py

import time
import logging
from src.weather_fetcher import fetch_all_weather_data
from src.weather_rollups import calculate_rollups
from src.alerting_system import check_alerts
from src.data_storage import create_table, save_weather_data
from src.visualization import visualize_weather_data

logging.basicConfig(level=logging.INFO)

def main():
    create_table()  # Create database table

    while True:
        weather_data = fetch_all_weather_data()
        if weather_data:
            rollup_data = calculate_rollups(weather_data)
            alerts = check_alerts(weather_data)
            save_weather_data(weather_data)

            # Log rollup data and alerts
            logging.info(f"Rollup Data: {rollup_data}")
            for alert in alerts:
                logging.warning(alert)

        time.sleep(300)  # Fetch every 5 minutes

if __name__ == "__main__":
    main()
