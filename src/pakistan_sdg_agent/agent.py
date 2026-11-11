import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from .models import SkillQuery, SkillRecommendation

class PakistanSDGAgent:
    def __init__(self, data_path: Optional[str] = None):
        if data_path is None:
            # Default path to sample JSON data
            data_path = Path(__file__).parent.parent.parent / "data" / "sample" / "it_skills_market.json"
        self.data_path = Path(data_path)
        self._load_data()

    def _load_data(self):
        if self.data_path.exists():
            with open(self.data_path, "r", encoding="utf-8") as f:
                self.market_data = json.load(f)
        else:
            self.market_data = {}

    def analyze_skills(self, query: SkillQuery) -> Dict[str, Any]:
        skills = self.market_data.get("skill_demand", [])
        recommendations = []
        
        for s in skills:
            recommendations.append({
                "skill": s["skill"],
                "demand_score": s["demand_score"],
                "avg_hourly_rate_usd": s["avg_hourly_rate_usd"],
                "sdg_alignment": s["sdg_alignment"],
                "recommendation": f"Aligned with Pakistan Vision 2035 & {query.target_sdg} in {query.location}."
            })
        
        return {
            "query": query.model_dump(),
            "market_trends": self.market_data.get("market_trends_2026", {}),
            "recommendations": recommendations
        }