from pakistan_sdg_agent.agent import PakistanSDGAgent
from pakistan_sdg_agent.models import SkillQuery

def test_agent_analysis():
    agent = PakistanSDGAgent()
    query = SkillQuery(sector="IT", target_sdg="SDG 8", location="Lahore")
    result = agent.analyze_skills(query)
    
    assert "market_trends" in result
    assert "recommendations" in result
    assert len(result["recommendations"]) > 0