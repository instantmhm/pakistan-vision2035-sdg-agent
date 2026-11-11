import streamlit as st
from pakistan_sdg_agent.agent import PakistanSDGAgent
from pakistan_sdg_agent.models import SkillQuery

st.set_page_config(
    page_title="Pakistan Vision 2035 & SDG AI Agent",
    page_icon="🇵🇰",
    layout="wide"
)

st.title("🇵🇰 Pakistan Vision 2035 & UN SDGs AI Agent")
st.markdown("Aligning tech skills, digital transformation, and economic growth with **Pakistan Vision 2035** and **UN SDGs (4, 8, 9)**.")

# Sidebar for user inputs
st.sidebar.header("Configuration")
sector = st.sidebar.selectbox("Select Economic Sector", ["IT", "AI & Data Science", "Renewable Energy", "E-Commerce", "Agri-Tech"])
sdg = st.sidebar.selectbox("Select UN SDG", ["SDG 8 (Decent Work & Growth)", "SDG 9 (Industry & Innovation)", "SDG 4 (Quality Education)"])
location = st.sidebar.text_input("Location / City", "Lahore")

if st.sidebar.button("Run Analysis", type="primary"):
    with st.spinner("Analyzing market trends and generating recommendations..."):
        agent = PakistanSDGAgent()
        # Clean sdg string to match expected format (e.g., "SDG 8")
        sdg_clean = sdg.split()[0] + " " + sdg.split()[1]
        query = SkillQuery(sector=sector, target_sdg=sdg_clean, location=location)
        result = agent.analyze_skills(query)
        
        st.success("Analysis Complete!")
        
        # Display Market Trends
        st.subheader("📊 Market Trends & Insights")
        trends = result.get("market_trends", {})
        cols = st.columns(len(trends))
        for i, (k, v) in enumerate(trends.items()):
            with cols[i]:
                st.metric(label=k.replace("_", " ").title(), value=v)
                
        # Display Recommendations
        st.subheader("💡 Actionable Skill Recommendations")
        for rec in result.get("recommendations", []):
            with st.expander(f"📌 {rec['skill']} (Demand Score: {rec['demand_score']})"):
                st.write(f"**Average Hourly Rate:** ${rec['avg_hourly_rate_usd']}/hr")
                st.write(f"**SDG Alignment:** {rec['sdg_alignment']}")
                st.write(f"**Recommendation:** {rec['recommendation']}")
st.markdown("---")
st.markdown("Built with Python, Pydantic, Rich, and Streamlit.")