import json
import sys
import datetime
import os
import re
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

def should_run_report():
    """Check if a bi-weekly report has already been generated in the last 14 days."""
    today = datetime.date.today()
    report_files = [f for f in os.listdir('.') if f.startswith('BiWeekly_Report_') and f.endswith('.md')]

    last_report_date = None
    for f in report_files:
        try:
            # Extract date from filename: BiWeekly_Report_YYYY-MM-DD.md
            date_str = f.replace('BiWeekly_Report_', '').replace('.md', '')
            report_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if last_report_date is None or report_date > last_report_date:
                last_report_date = report_date
        except ValueError:
            continue

    if last_report_date:
        days_since_last = (today - last_report_date).days
        if days_since_last < 14:
            print(f"Skipping run. Last report was generated {days_since_last} days ago on {last_report_date}. Next run due in {14 - days_since_last} days.")
            return False

    return True

def main():
    print("System starting...")

    if not should_run_report():
        sys.exit(0)

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
