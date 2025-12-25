import time
import sys
from content_agent import ContentAgent
from ad_agent import AdAgent
from health_agent import HealthAgent

class Orchestrator:
    def __init__(self):
        self.content_agent = ContentAgent()
        self.ad_agent = AdAgent()
        self.health_agent = HealthAgent()
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
        print("===========================================")

        for i in range(cycles):
            self.cycle_count += 1
            print(f"\n--- Cycle {self.cycle_count} Started ---")

            # Step 1: Health Check
            if not self.health_agent.run_diagnostics():
                print("[Orchestrator] System unstable. Aborting cycle.")
                break

            # Step 2: Content Creation
            print("[Orchestrator] Triggering Content Agent...")
            self.content_agent.publish()

            # Step 3: Monetization
            print("[Orchestrator] Triggering Ad Agent...")
            self.ad_agent.place_ad()

            print(f"--- Cycle {self.cycle_count} Completed ---")
            # In a real infinite loop, we would sleep here
            # time.sleep(3600)

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
