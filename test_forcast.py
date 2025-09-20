import unittest
from forecast_muncie import get_forecast_url, get_forecast_data

class TestForecast(unittest.TestCase):
    def test_forecast_url(self):
        url = get_forecast_url()
        self.assertTrue(url.startswith("https://api.weather.gov/gridpoints/"))

    def test_forecast_periods(self):
        url = get_forecast_url()
        periods = get_forecast_data(url)
        self.assertEqual(len(periods), 14)
        for period in periods:
            self.assertIn('name', period)
            self.assertIn('temperature', period)
            self.assertIn('detailedForecast', period)

if __name__ == "__main__":
    unittest.main()
