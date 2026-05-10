from datetime import datetime, timezone
from sqlalchemy import Integer, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class Biometrics(Base):
    __tablename__ = "biometrics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    weight: Mapped[float] = mapped_column(Float, nullable=True, comment="Weight in kilograms")
    height: Mapped[int] = mapped_column(Integer, nullable=True, comment="Height in centimeters")
    pulse: Mapped[int] = mapped_column(Integer, nullable=True, comment="Resting heart rate in bpm")
    calories_burned: Mapped[float] = mapped_column(Float, nullable=True, comment="Total calories burned")

    recorded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )