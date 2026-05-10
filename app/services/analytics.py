from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta, timezone
from app.models.biometrics import Biometrics

class AnalyticsService:
    @staticmethod
    async def get_weekly_summary(db: AsyncSession):
        """
        Считает средний вес и пульс за последние 7 дней.
        """
        one_week_ago = datetime.now(timezone.utc) - timedelta(days=7)
        
        # Строим сложный запрос с агрегатными функциями AVG
        query = select(
            func.avg(Biometrics.weight).label("avg_weight"),
            func.avg(Biometrics.pulse).label("avg_pulse"),
            func.count(Biometrics.id).label("records_count")
        ).where(Biometrics.recorded_at >= one_week_ago)
        
        result = await db.execute(query)
        # Получаем первую (и единственную) строку результата
        summary = result.one()
        
        return {
            "average_weight": round(summary.avg_weight, 2) if summary.avg_weight else 0,
            "average_pulse": round(summary.avg_pulse, 1) if summary.avg_pulse else 0,
            "total_records": summary.records_count
        }