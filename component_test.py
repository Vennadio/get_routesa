import unittest
import requests
import re

class TestTabulation(unittest.TestCase):

    def test_tabulation(self):
        with open('routes_service.py', 'r') as f:
            lines = f.readlines()
            for idx, line in enumerate(lines, start=1):
                self.assertTrue(re.match(r'^\t', line), f"Tabulation missing in line {idx}")


if __name__ == '__main__':
    unittest.main()

