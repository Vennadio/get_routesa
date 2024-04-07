import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import patch

from main import app, FIRST_SERVICE_URL

@pytest.mark.asyncio
async def test_process_stops():
    test_stops_data = [{"name": "stop1", "location": "location1"}, {"name": "stop2", "location": "location2"}]
    
    # Мокируем запрос к первому сервису
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = test_stops_data
        
        # Проверяем обработку данных
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/processed_stops/")
            assert response.status_code == 200
            processed_stops = response.json()
            assert processed_stops == [{"name": "STOP1", "location": "location1"}, {"name": "STOP2", "location": "location2"}]
            
        mock_get.assert_called_once_with(FIRST_SERVICE_URL)

@pytest.mark.asyncio
async def test_process_stops_error():
    # Мокируем запрос к первому сервису для имитации ошибки
    with patch("requests.get") as mock_get:
        mock_get.side_effect = Exception("Test error")
        
        # Проверяем обработку ошибки
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/processed_stops/")
            assert response.status_code == 500
            assert "Error while fetching stops data" in response.text
