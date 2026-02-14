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
from utils.colors import Colors

def load_data(filepath="links.json"):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(Colors.style(f"Error: File '{filepath}' not found.", Colors.FAIL))
        return []

def is_scheduled_run():
    """
    Checks if the current date is scheduled for a bi-weekly run.
    Schedule: Every other Monday (Even weeks).
    Returns: (bool, str) -> (should_run, reason_or_status)
    """
    today = datetime.date.today()
    year, week, weekday = today.isocalendar()

    # Run on Mondays (weekday == 1) of even weeks
    if weekday == 1 and week % 2 == 0:
        return True, f"Week {week} (Even), Monday"

    return False, f"Week {week}, Day {weekday}"

def main():
    start_time = time.time()
    print(Colors.style(f"{Colors.ROCKET} System starting...", Colors.HEADER, bold=True))

    # Check Schedule
    should_run, schedule_info = is_scheduled_run()

    if not should_run:
        msg = f"Skipping run: Scheduled for Bi-Weekly (Even Mondays). Current: {schedule_info}"
        print(Colors.style(f"{Colors.CALENDAR} {msg}", Colors.WARNING))

        # Summary for skipped run
        Colors.print_summary("SYSTEM SKIPPED", {
            f"{Colors.TIME} Duration": f"{time.time() - start_time:.2f}s",
            f"{Colors.INFO} Reason": "Not scheduled day",
            f"{Colors.CALENDAR} Current": schedule_info
        })
        return

    data = load_data()
    if not data:
        print(Colors.style("No data available. Exiting.", Colors.FAIL))
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
    report_title = f"Bi-Weekly Autonomous Agent Report - {datetime.date.today()}"
    full_report = f"# {report_title}\n\n"
    success_count = 0
    fail_count = 0

    print(Colors.style(f"{Colors.GEAR} Running {len(agents)} agents...", Colors.BLUE))

    for agent in agents:
        try:
            output = agent.run(data)
            full_report += f"{output}\n---\n"
            success_count += 1
        except Exception as e:
            print(Colors.style(f"{Colors.CROSS} Error running {agent.name}: {e}", Colors.FAIL))
            full_report += f"### {agent.name}\nError: {e}\n\n---\n"
            fail_count += 1

    # Save report
    filename = f"Bi-Weekly_Report_{datetime.date.today()}.md"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_report)
        report_status = filename
    except Exception as e:
        print(Colors.style(f"Failed to write report: {e}", Colors.FAIL))
        report_status = "Failed"

    end_time = time.time()
    duration = end_time - start_time

    # Summary
    summary_data = {
        f"{Colors.TIME} Duration": f"{duration:.2f}s",
        f"{Colors.DOC} Report": report_status,
        f"{Colors.CHECK} Agents OK": str(success_count),
    }

    if fail_count > 0:
        summary_data[f"{Colors.CROSS} Agents Fail"] = Colors.style(str(fail_count), Colors.FAIL)

    Colors.print_summary("SYSTEM RUN COMPLETE", summary_data)

if __name__ == "__main__":
    main()
