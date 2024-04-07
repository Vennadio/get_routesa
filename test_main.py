import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch
from routes_service import app  # Предположим, что ваш файл с сервисом называется my_service.py


class TestMyServiceIntegration(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    @patch("my_service.requests.get") 
    def test_process_stops_integration(self, mock_get):
        # Мокируем ответ от внешнего сервиса
        mock_get.return_value.json.return_value = [
            {"name": "stop1", "location": [1.23, 4.56]},
            {"name": "stop2", "location": [7.89, 0.12]}
        ]

        # Отправляем GET-запрос к нашему сервису
        response = self.client.get("/processed_stops/")

        # Проверяем, что запрос к внешнему сервису был выполнен
        mock_get.assert_called_once_with("http://stops-service:8000/stops/")

        # Проверяем успешность ответа от нашего сервиса
        self.assertEqual(response.status_code, 200)

        # Проверяем, что обработанные остановки были возвращены
        expected_processed_stops = [
            {"name": "STOP1", "location": [1.23, 4.56]},
            {"name": "STOP2", "location": [7.89, 0.12]}
        ]
        self.assertEqual(response.json(), expected_processed_stops)


if __name__ == "__main__":
    unittest.main()
