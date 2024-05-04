import unittest
import importlib.util
from pathlib import Path

class TestSyntax(unittest.TestCase):
    def test_syntax(self):
        file_path = Path("routes_service.py")
        spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        self.assertIsNotNone(module)
    
    def test_syntax1(self):
        file_path = Path("routes_service.py")
        spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        self.assertIsNotNone(module)
    
    def check_response(self):
        file_path = Path("routes_service.py")
        spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        self.assertIsNotNone(module)

if __name__ == "__main__":
    unittest.main()