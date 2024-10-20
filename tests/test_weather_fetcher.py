# tests/test_weather_fetcher.py

import unittest
from unittest.mock import patch
from src.weather_fetcher import fetch_weather_data

class TestWeatherFetcher(unittest.TestCase):
    
    @patch('src.weather_fetcher.requests.get')
    def test_fetch_weather_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'main': {'temp': 25, 'humidity': 60},
            'weather': [{'description': 'clear sky'}],
            'wind': {'speed': 5}
        }
        result = fetch_weather_data("Delhi")
        self.assertEqual(result['main']['temp'], 25)
        self.assertEqual(result['weather'][0]['description'], 'clear sky')

    @patch('src.weather_fetcher.requests.get')
    def test_fetch_weather_data_failure(self, mock_get):
        mock_get.side_effect = Exception("Error fetching data")
        result = fetch_weather_data("Delhi")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
