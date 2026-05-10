from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class BiometricsBase(BaseModel):
    weight: float | None = Field(None, description="Weight in kilograms", gt=0, lt=300)
    height: int | None = Field(None, description="Height in centimeters", gt=50, lt=250)
    pulse: int | None = Field(None, description="Resting heart rate in bpm", gt=30, lt=250)
    calories_burned: float | None = Field(None, description="Total calories burned", ge=0)

class BiometricsCreate(BiometricsBase):
    pass

class BiometricsResponse(BiometricsBase):
    id: int
    recorded_at: datetime

    model_config = ConfigDict(from_attributes=True)