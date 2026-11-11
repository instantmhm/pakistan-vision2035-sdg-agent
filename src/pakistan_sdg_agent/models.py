from pydantic import BaseModel, Field
from typing import List, Optional

class SkillQuery(BaseModel):
    sector: str = Field(..., description="Target sector like IT, Agriculture, or Renewable Energy")
    target_sdg: str = Field(..., description="Target UN SDG, e.g., SDG 8, SDG 9")
    location: str = Field(..., description="City or region in Pakistan")

class SkillRecommendation(BaseModel):
    skill: str
    demand_score: int
    avg_hourly_rate_usd: float
    sdg_alignment: str
    recommendation: str