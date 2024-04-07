import unittest
import importlib.util
from pathlib import Path

class TestSyntax(unittest.TestCase):
    def test_syntax(self):
        file_path = Path("routes_service.py")
        spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Проверяем, что код успешно загружен
        self.assertIsNotNone(module)

if __name__ == "__main__":
    unittest.main()
