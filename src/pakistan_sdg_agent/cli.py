import typer
from rich import print
from .agent import PakistanSDGAgent
from .models import SkillQuery

app = typer.Typer(help="Pakistan Vision 2035 & SDG AI Agent CLI")

@app.callback(invoke_without_command=True)
def main(
    sector: str = typer.Option("IT", help="Target economic sector"),
    sdg: str = typer.Option("SDG 8", help="Target UN SDG"),
    location: str = typer.Option("Lahore", help="City or region in Pakistan")
):
    """
    Analyze skill demand and market trends aligned with Pakistan Vision 2035 & UN SDGs.
    """
    print(f"[bold cyan]Analyzing sector '{sector}' for {sdg} in {location}...[/bold cyan]\n")
    
    agent = PakistanSDGAgent()
    query = SkillQuery(sector=sector, target_sdg=sdg, location=location)
    result = agent.analyze_skills(query)
    
    print("[bold green]=== Market Trends & Insights ===[/bold green]")
    trends = result.get("market_trends", {})
    for k, v in trends.items():
        print(f"  - {k}: [yellow]{v}[/yellow]")
    
    print("\n[bold green]=== Skill Recommendations ===[%/bold green]")
    for rec in result.get("recommendations", []):
        print(f"  * [bold]{rec['skill']}[/bold]")
        print(f"    Demand Score: {rec['demand_score']} | Avg Rate: ${rec['avg_hourly_rate_usd']}/hr")
        print(f"    SDG: {rec['sdg_alignment']}")
        print(f"    Note: {rec['recommendation']}\n")

if __name__ == "__main__":
    app()