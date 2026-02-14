import json
import sys
import datetime
from agents.analysis_agent import AnalysisAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.content_agent import ContentAgent
from agents.health_check_agent import HealthCheckAgent
from agents.monetization_agent import MonetizationAgent
from agents.creativity_agent import CreativityAgent
from agents.ads_agent import AdsAgent

def load_data(filepath="links.json"):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []

def main():
    print("System starting...")
    data = load_data()
    if not data:
        print("No data available. Exiting.")
        sys.exit(1)

    # Instantiate agents
    # Stage 1: Insight Generators (Research, Intelligence, Analysis, Health, Monetization)
    insight_agents = [
        AnalysisAgent(),
        ResearchAgent(),
        IntelligenceAgent(),
        HealthCheckAgent(),
        MonetizationAgent()
    ]

    # Stage 2: Action Takers (Content, Ads, Creativity) - These consume context
    action_agents = [
        ContentAgent(),
        AdsAgent(),
        CreativityAgent()
    ]

    # Context to share between agents
    context = {}

    # Run agents and collect output
    full_report = f"# Daily Autonomous Agent Report - {datetime.date.today()}\n\n"

    # Run Stage 1
    print("--- Running Stage 1: Insights ---")
    for agent in insight_agents:
        try:
            output = agent.run(data, context)
            context[agent.name] = output # Share output in context
            full_report += f"{output}\n---\n"
        except Exception as e:
            print(f"Error running {agent.name}: {e}")
            full_report += f"### {agent.name}\nError: {e}\n\n---\n"

    # Run Stage 2
    print("--- Running Stage 2: Actions (with Context) ---")
    for agent in action_agents:
        try:
            output = agent.run(data, context)
            full_report += f"{output}\n---\n"
        except Exception as e:
            print(f"Error running {agent.name}: {e}")
            full_report += f"### {agent.name}\nError: {e}\n\n---\n"

    # Save report
    filename = f"Daily_Report_{datetime.date.today()}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_report)

    print(f"System run complete. Report saved to {filename}")

if __name__ == "__main__":
    main()
