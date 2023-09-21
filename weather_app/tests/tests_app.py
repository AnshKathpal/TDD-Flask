import unittest
from app import app

class WeatherAppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_valid_city_weather(self):
        response = self.client.get('/weather/San%20Francisco/')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'temperature': 14, 'weather': 'Cloudy'})

    def test_get_invalid_city_weather(self):
        response = self.client.get('/weather/InvalidCity/')
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data, {'error': 'City not found'})

if __name__ == '__main__':
    unittest.main()
