from fastapi import HTTPException
from requests.exceptions import RequestException
from unittest.mock import MagicMock
import pytest

from your_module import app, FIRST_SERVICE_URL, process_stops

@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch('/processed_stops/')
    yield mock

def test_process_stops(mock_requests_get):
    # Устанавливаем мок для успешного запроса
    mock_requests_get.return_value.json.return_value = [{"name": "stop1", "location": "location1"}, {"name": "stop2", "location": "location2"}]

    # Вызываем функцию для обработки остановок
    processed_stops = process_stops()

    # Проверяем, что запрос был отправлен к правильному URL
    mock_requests_get.assert_called_once_with(FIRST_SERVICE_URL)

    # Проверяем, что данные обработаны правильно
    assert processed_stops == [{"name": "STOP1", "location": "location1"}, {"name": "STOP2", "location": "location2"}]

def test_process_stops_error(mock_requests_get):
    # Устанавливаем мок для исключения при запросе
    mock_requests_get.side_effect = RequestException("Test error")

    # Проверяем, что возникает HTTPException при ошибке запроса
    with pytest.raises(HTTPException) as exc_info:
        process_stops()

    assert exc_info.value.status_code == 500
    assert "Error while fetching stops data" in str(exc_info.value)
