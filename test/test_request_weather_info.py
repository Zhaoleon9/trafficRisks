import unittest
from src.request_weather_info import Weather


class TestRequestWeatherInfo(unittest.TestCase):
    """Unit tests for request weather info class"""
    @classmethod
    def setUpClass(cls):
        cls.calc = Weather()

    def test_get_wind_speed(self):
        self.assertIsNotNone(self.calc.get_wind_speed())

    def test_get_snow_precipitation(self):
        self.assertIsNotNone(self.calc.get_snow_precipitation())


if __name__ == "__main__":
    unittest.main()
