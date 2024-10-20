# Real Time Weather Monitoring System

## Project Overview

This project is a **Real Time Weather Monitoring System** that fetches live weather data from the [OpenWeatherMap API](https://openweathermap.org/), processes it to compute daily summaries (averages, maximum, minimum temperatures, and dominant weather conditions), and provides alerting mechanisms when certain thresholds (e.g., temperature or weather condition limits) are breached. Additionally, the system visualizes weather trends and can be customized to fetch weather data at user-defined intervals.

## Key Features

1. **Real-Time Data Fetching**:
   - Continuously retrieves weather data for six Indian metros: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
   - Customizable time intervals for weather data retrieval.
   
2. **Weather Data Processing**:
   - Converts temperature values from Kelvin to Celsius (and Fahrenheit if needed).
   - Aggregates daily weather data and provides:
     - Average temperature
     - Maximum and minimum temperature
     - Dominant weather condition (based on frequency of occurrences).

3. **Threshold-based Alerting**:
   - Configurable thresholds for temperature or specific weather conditions.
   - Alerts are triggered when thresholds are exceeded (e.g., temperature above 35°C for two consecutive updates).

4. **Data Storage**:
   - Weather data is persisted in an SQLite database for further analysis and review.

5. **Visualization**:
   - Displays daily weather summaries and historical trends using Matplotlib.
   - Can visualize temperature trends, dominant weather conditions, and more.


## Installation and Setup

### Prerequisites

- Python 3.8+
- A valid [OpenWeatherMap API Key](https://home.openweathermap.org/users/sign_up)
- Docker if you prefer running the application in a container.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd weather-monitoring-system
```

### 2. Create a Virtual Environment 

```bash
python3 -m venv venv
source venv/bin/activate  
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

```bash
API_KEY = 'your-api-key-here'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']  # Metros in India
TEMP_THRESHOLD = 35  # Example threshold for temperature alerts
INTERVAL = 300  # Fetch interval in seconds (default: every 5 minutes)
```

### 5. Run the Application

After setting up everything, run the main script:

```bash
python src/main.py
```

### 6. Visualizing Data

To view historical trends and weather summaries, run:

```bash
python src/visualization.py
```

## Alerting System

The system allows users to configure alerts based on the temperature or weather conditions. You can set these thresholds in `config/config.py`. 
Alerts will be displayed in the console or logged in the `logs/app.log file` file.

## Testing

The project includes unit tests to validate key functionalities. 
To run the tests:

```bash
python -m unittest discover -s tests
```

### Tests include:
- Weather Fetcher: Tests the API integration and correct parsing of data.
- Temperature Conversion: Tests conversion from Kelvin to Celsius.
- Alerting System: Ensures alerts are triggered correctly when thresholds are breached.
- Rollups and Aggregates: Tests daily weather summary calculations.

## Docker Setup

To run the application in a Docker container:

Build the Docker image:
```bash
docker build -t weather-monitoring-system .
```

Run the container:
```bash
docker run -d weather-monitoring-system
```

## Future Improvements
- Additional Weather Parameters: Extend the system to fetch and process additional weather data such as humidity, wind speed, and precipitation.
- Weather Forecasting: Incorporate weather forecasts from the OpenWeatherMap API to generate future trends and predictions.
- Email/SMS Alerts: Add functionality to send email or SMS notifications when weather thresholds are breached.

## License
- This project is licensed under the MIT License. See the `LICENSE` file for details.

