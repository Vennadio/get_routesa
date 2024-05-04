import routes_service
import unittest
import requests

class TestYourService(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_processed_stops_endpoint(self):

        url = "http://localhost:8000/processed_stops/" 
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(isinstance(response.json(), list))

if __name__ == '__main__':
    unittest.main()

