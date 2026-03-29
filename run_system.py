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
    agents = [
        AnalysisAgent(),
        ResearchAgent(),
        IntelligenceAgent(),
        ContentAgent(),
        HealthCheckAgent(),
        MonetizationAgent(),
        CreativityAgent()
    ]

    # Run agents and collect output
    full_report = f"# Bi-Weekly Autonomous Agent Report - {datetime.date.today()}\n\n"

    for agent in agents:
        try:
            output = agent.run(data)
            full_report += f"{output}\n---\n"
        except Exception as e:
            print(f"Error running {agent.name}: {e}")
            full_report += f"### {agent.name}\nError: {e}\n\n---\n"

    # Save report
    filename = f"BiWeekly_Report_{datetime.date.today()}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_report)

    print(f"System run complete. Report saved to {filename}")

if __name__ == "__main__":
    main()
