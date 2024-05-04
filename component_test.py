import unittest
import requests

class TestTabulation(unittest.TestCase):

    def test_tabulation(self):
        with open('routes_service.py', 'r') as f:
            lines = f.readlines()
            for idx, line in enumerate(lines, start=1):
                self.assertTrue(re.match(r'^\t', line), f"Tabulation missing in line {idx}")

class TestHTTP(unittest.TestCase):

    def test_process_stops_http(self):
        response = requests.get("http://localhost:8000/processed_stops/") 
        self.assertEqual(response.status_code, 200, "HTTP request failed")

if __name__ == '__main__':
    unittest.main()

