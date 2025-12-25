import time
import random
from src.core.message_bus import MessageBus
from src.core.memory import Memory
from src.agents.research_analyze import ResearchAgent, AnalyzeAgent
from src.agents.content_creative import ContentAgent, CreativityAgent
from src.agents.ad_monetization import AdAgent, MonetizationAgent
from src.agents.health_intelligence import HealthAgent, IntelligenceAgent

def main():
    print("Initializing Autonomous Agent System...")

    # Core Infrastructure
    bus = MessageBus()
    memory = Memory()

    # Instantiate Agents
    agents = [
        ResearchAgent("Researcher", bus, memory),
        AnalyzeAgent("Analyst", bus, memory),
        ContentAgent("Writer", bus, memory),
        CreativityAgent("Artist", bus, memory),
        AdAgent("AdManager", bus, memory),
        MonetizationAgent("CFO", bus, memory),
        HealthAgent("Medic", bus, memory),
        IntelligenceAgent("Overlord", bus, memory)
    ]

    print(f"Deployed {len(agents)} agents.")
    print("Starting Autonomous Loop (Press Ctrl+C to stop)...")

    try:
        # Simulation loop
        # running for a fixed number of iterations for demonstration
        for i in range(20):
            print(f"\n--- Cycle {i+1} ---")

            # 1. Allow agents to act autonomously
            for agent in agents:
                agent.act()

            # 2. Allow agents to learn/reflect
            if i % 5 == 0:
                print("\n--- Learning Phase ---")
                for agent in agents:
                    agent.learn()

            # Simulate time passage
            time.sleep(1)

    except KeyboardInterrupt:
        print("System stopping...")

    # Save final state
    memory.save()
    print("\nSystem state saved. Shutdown complete.")

if __name__ == "__main__":
    main()
