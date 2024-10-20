# tests/test_alerting.py

import unittest
from src.alerting_system import check_alerts

class TestAlertingSystem(unittest.TestCase):
    
    def test_alerts(self):
        weather_data = {
            'Delhi': {'temperature': 36},
            'Mumbai': {'temperature': 28},
        }
        alerts = check_alerts(weather_data)
        self.assertIn("Alert: Delhi temperature is above 35°C: 36°C", alerts)
        self.assertNotIn("Alert: Mumbai temperature is above 35°C", alerts)

if __name__ == '__main__':
    unittest.main()
