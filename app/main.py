from fastapi import FastAPI
from app.core.config import settings
from app.api import biometrics

def create_app() -> FastAPI:
    # Инициализируем приложение с нашими настройками из .env
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="Core API for Health & Fitness tracking"
    )

    app.include_router(biometrics.router, prefix='/api/v1/biometrics', tags=['Biometrics'])

    # Простейший эндпоинт проверки здоровья сервера (Healthcheck)
    @app.get("/ping", tags=["System"])
    async def ping():
        return {
            "status": "ok", 
            "project": settings.PROJECT_NAME,
            "message": "Virtus Fit API is running!"
        }

    return app

# ВОТ ЭТА СТРОЧКА САМАЯ ГЛАВНАЯ! 
# Именно эту переменную "app" ищет Uvicorn
app = create_app()