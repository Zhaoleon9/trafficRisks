import unittest
import sys
import os
import pandas as pd

# Add the "src" directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from climate_data_analysis import ClimateData

class TestClimateData(unittest.TestCase):
    """Unit tests for the ClimateData class."""
    @classmethod
    def setUpClass(cls):
        cls.calc = ClimateData()
    
    def test_get_wind_speed(self):
        self.assertIsInstance(self.calc.get_wind_speed(), pd.Series)

    def test_get_snow_precip(self):
        self.assertIsInstance(self.calc.get_snow_precip(), pd.Series)
    
    def test_get_wind_proportion(self):
        self.assertGreaterEqual(self.calc.get_wind_proportion(0.2),0)
    
    def test_get_wind_proportion_by_negative(self):
        self.assertEqual(self.calc.get_wind_proportion(-1), 0)

    def test_get_snow_proportion(self):
        self.assertGreaterEqual(self.calc.get_wind_proportion(0.2),0)
    
    def test_get_snow_proportion_by_over(self):
        self.assertEqual(self.calc.get_wind_proportion(5), 0)
        
if __name__ == "__main__":
    unittest.main()
