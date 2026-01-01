import time
import sys
from content_agent import ContentAgent
from ad_agent import AdAgent
from health_agent import HealthAgent
from creative_agent import CreativeAgent

class Orchestrator:
    def __init__(self):
        self.content_agent = ContentAgent()
        self.ad_agent = AdAgent()
        self.health_agent = HealthAgent()
        self.creative_agent = CreativeAgent()
        self.cycle_count = 0

    def start_autonomous_loop(self, cycles=1):
        """
        Run the autonomous agents in a coordinated loop.
        :param cycles: Number of cycles to run (to prevent infinite loop in sandbox).
        """
        print("=== Initializing Autonomous Agent Network ===")
        print("Integration: 100%")
        print("Autonomy: 100%")
        print("Collaborative Intelligence: ACTIVE")
        print("Daily Work Protocol: ENGAGED")
        print("===========================================")

        for i in range(cycles):
            self.cycle_count += 1
            print(f"\n--- Cycle {self.cycle_count} (Simulated Day) Started ---")

            # Step 1: Health Check
            if not self.health_agent.run_diagnostics():
                print("[Orchestrator] System unstable. Aborting cycle.")
                break

            # Step 2: Creative Brainstorming (Curiosity & Ideas)
            print("[Orchestrator] Triggering Creative Agent (100% Curiosity)...")
            self.creative_agent.implement_idea()

            # Step 3: Content Creation (Intelligence)
            print("[Orchestrator] Triggering Content Agent...")
            self.content_agent.publish()

            # Step 4: Monetization (Sustainability)
            print("[Orchestrator] Triggering Ad Agent...")
            self.ad_agent.place_ad()

            print(f"--- Cycle {self.cycle_count} Completed with High Solution Interest ---")

            # In a real infinite loop, we would sleep here
            # time.sleep(86400) # 24 hours

        print("\n=== Autonomous Operations Sequence Finished ===")

if __name__ == "__main__":
    # Check if a cycle count argument is provided
    cycles = 1
    if len(sys.argv) > 1:
        try:
            cycles = int(sys.argv[1])
        except ValueError:
            pass

    orchestrator = Orchestrator()
    orchestrator.start_autonomous_loop(cycles)
