from autonomous_agents.researcher import ResearcherAgent
from autonomous_agents.analyst import AnalystAgent
from autonomous_agents.creator import ContentCreatorAgent
from autonomous_agents.ads import AdAgent
from autonomous_agents.health import HealthAgent
from autonomous_agents.google_colab import GoogleColabAgent
import time

def main():
    print("Initializing Autonomous System...")

    # Initialize Agents
    agents = [
        HealthAgent(),
        ResearcherAgent(),
        AnalystAgent(),
        ContentCreatorAgent(),
        AdAgent(),
        GoogleColabAgent()
    ]

    context = {}

    # Collaborative Loop
    print("\n--- Starting Collaborative Workflow ---")
    for agent in agents:
        print(f"\n[Agent: {agent.name}] Activated.")
        agent.run(context)
        print(f"[Agent: {agent.name}] Finished task.")

    print("\n--- Workflow Complete ---")
    print("\nFinal Context State:")
    for k, v in context.items():
        print(f"{k}: {str(v)[:100]}...") # Truncate for display

if __name__ == "__main__":
    main()
