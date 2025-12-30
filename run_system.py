import json
import sys
import datetime
import time
from agents.analysis_agent import AnalysisAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.content_agent import ContentAgent
from agents.health_check_agent import HealthCheckAgent
from agents.monetization_agent import MonetizationAgent
from agents.creativity_agent import CreativityAgent

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_data(filepath="links.json"):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{Colors.FAIL}Error: File '{filepath}' not found.{Colors.ENDC}")
        return []

def print_summary_box(results):
    print(f"\n{Colors.HEADER}╔══════════════════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.HEADER}║                 SYSTEM RUN SUMMARY                   ║{Colors.ENDC}")
    print(f"{Colors.HEADER}╠══════════════════════════════════════════════════════╣{Colors.ENDC}")

    for name, status in results:
        # Determine color and icon based on status
        if status == "Success":
            icon = "✓"
            color = Colors.OKGREEN
        else:
            icon = "✗"
            color = Colors.FAIL

        # Calculate padding for alignment
        # Inner width is 54 chars
        # Content structure: " " (1) + Icon (1) + " " (1) + Name (N) + Padding (P)
        # 1 + 1 + 1 + N + P = 54  =>  P = 51 - N
        padding = 51 - len(name)
        if padding < 0: padding = 0

        line = f"║ {color}{icon} {name}{Colors.ENDC}" + " " * padding + f"{Colors.HEADER}║{Colors.ENDC}"
        print(line)

    print(f"{Colors.HEADER}╚══════════════════════════════════════════════════════╝{Colors.ENDC}\n")

def main():
    print(f"{Colors.BOLD}{Colors.OKCYAN}🚀 System starting...{Colors.ENDC}\n")
    data = load_data()
    if not data:
        print(f"{Colors.FAIL}No data available. Exiting.{Colors.ENDC}")
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
    full_report = f"# Daily Autonomous Agent Report - {datetime.date.today()}\n\n"
    results = []

    for agent in agents:
        print(f"{Colors.OKBLUE}⚡ Running {agent.name}...{Colors.ENDC}")
        try:
            # Adding a small delay to simulate work and make the UX feel less "instant dump"
            time.sleep(0.5)
            output = agent.run(data)
            full_report += f"{output}\n---\n"
            print(f"{Colors.OKGREEN}  ✓ {agent.name} completed successfully.{Colors.ENDC}\n")
            results.append((agent.name, "Success"))
        except Exception as e:
            print(f"{Colors.FAIL}  ✗ Error running {agent.name}: {e}{Colors.ENDC}\n")
            full_report += f"### {agent.name}\nError: {e}\n\n---\n"
            results.append((agent.name, "Failed"))

    # Save report
    filename = f"Daily_Report_{datetime.date.today()}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_report)

    print_summary_box(results)
    print(f"{Colors.BOLD}📄 Report saved to: {Colors.UNDERLINE}{filename}{Colors.ENDC}")

if __name__ == "__main__":
    main()
