from typing import List
from sqlalchemy import select
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.biometrics import Biometrics
from app.schemas.biometrics import BiometricsCreate, BiometricsResponse
from app.services.analytics import AnalyticsService
import json
from app.db.redis import get_redis


# Создаем роутер (группу эндпоинтов)
router = APIRouter()

# Создаем POST-запрос
@router.post("/", response_model=BiometricsResponse)
async def add_biometrics(
    data: BiometricsCreate, 
    db: AsyncSession = Depends(get_db) # Dependency Injection!
):
    """
    Добавить новые биометрические данные.
    """
    # 1. Превращаем Pydantic-схему в словарь (model_dump) и распаковываем (**)
    new_metric = Biometrics(**data.model_dump())
    
    # 2. Добавляем в транзакцию
    db.add(new_metric)
    
    # 3. Сохраняем в базу
    await db.commit()
    
    # 4. Обновляем объект, чтобы получить сгенерированный базой id и recorded_at
    await db.refresh(new_metric)
    
    # FastAPI автоматически превратит этот объект обратно в JSON благодаря BiometricsResponse
    return new_metric

@router.get("/", response_model=List[BiometricsResponse])
async def get_biometrics_history(
    limit: int = 10,
    offset: int = 0,
    db: AsyncSession = Depends(get_db)
):
    """
    Получить историю биометрических данных (с пагинацией и сортировкой по новизне).
    """
    query = (
        select(Biometrics)
        .order_by(Biometrics.recorded_at.desc()) # Сначала самые свежие записи
        .offset(offset)
        .limit(limit)
    )
    
    # Выполняем асинхронный запрос к БД
    result = await db.execute(query)
    
    # Извлекаем объекты из ответа БД
    metrics = result.scalars().all()
    
    return metrics

@router.get("/summary", tags=["Analytics"])
async def get_biometrics_summary(
    db: AsyncSession = Depends(get_db)
):
    """
    Получить аналитическую сводку (средний вес, пульс и кол-во записей) за неделю.
    """
    # Вызываем наш статический метод сервиса
    summary = await AnalyticsService.get_weekly_summary(db)
    return summary


@router.get("/summary", tags=["Analytics"])
async def get_biometrics_summary(
    db: AsyncSession = Depends(get_db),
    redis = Depends(get_redis) # Подключаем Redis
):
    cache_key = "weekly_summary"
    
    cached_data = await redis.get(cache_key)
    if cached_data:
        return json.loads(cached_data) # Если есть в кеше — возвращаем сразу
    
    summary = await AnalyticsService.get_weekly_summary(db)
    
    await redis.set(cache_key, json.dumps(summary), ex=60)
    
    return summary