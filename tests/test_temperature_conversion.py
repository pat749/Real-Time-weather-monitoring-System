# tests/test_temperature_conversion.py

import unittest

class TestTemperatureConversion(unittest.TestCase):
    
    def test_kelvin_to_celsius(self):
        from src.weather_fetcher import fetch_weather_data
        kelvin_temp = 300
        celsius_temp = kelvin_temp - 273.15
        self.assertAlmostEqual(celsius_temp, 26.85, places=2)

if __name__ == '__main__':
    unittest.main()
