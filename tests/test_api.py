import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_get_biometrics_summary():
    """
    Тестируем эндпоинт аналитики (статистики)
    """
    # Создаем виртуального клиента для тестирования нашего FastAPI приложения
    transport = ASGITransport(app=app)
    
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Делаем GET запрос к нашему маршруту
        response = await ac.get("/api/v1/biometrics/summary")
    
    # 1. Проверяем, что сервер ответил без ошибок (HTTP 200 OK)
    assert response.status_code == 200
    
    # 2. Получаем JSON-ответ от сервера
    data = response.json()
    
    # 3. Проверяем, что в ответе есть нужные нам ключи (даже если там нули)
    assert "average_weight" in data
    assert "average_pulse" in data
    assert "total_records" in data