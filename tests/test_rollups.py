# tests/test_rollups.py

import unittest
from src.weather_rollups import calculate_rollups

class TestRollups(unittest.TestCase):
    
    def test_calculate_rollups(self):
        weather_data = {
            'Delhi': {'temperature': 30, 'condition': 'clear sky'},
            'Mumbai': {'temperature': 28, 'condition': 'light rain'},
            'Chennai': {'temperature': 32, 'condition': 'clear sky'}
        }
        rollup = calculate_rollups(weather_data)
        self.assertAlmostEqual(rollup['average_temp'], 30.0)
        self.assertEqual(rollup['dominant_condition'], 'clear sky')

if __name__ == '__main__':
    unittest.main()
