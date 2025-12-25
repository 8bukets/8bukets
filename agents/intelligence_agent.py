from agents.base_agent import BaseAgent
import psutil
import json
import os
from datetime import datetime

class HealthAgent(BaseAgent):
    def __init__(self, name: str = "Health"):
        super().__init__(name)

    async def process(self, data: dict) -> dict:
        self.log("Performing system health check...")

        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        status = "Healthy"
        if cpu_usage > 90 or memory_usage > 90:
            status = "Critical"
        elif cpu_usage > 70 or memory_usage > 70:
            status = "Warning"

        report = {
            "cpu": f"{cpu_usage}%",
            "memory": f"{memory_usage}%",
            "disk": f"{disk_usage}%",
            "overall_status": status,
            "timestamp": datetime.now().isoformat()
        }

        self.log(f"Health Status: {status} (CPU: {cpu_usage}%, Mem: {memory_usage}%)")
        return {"status": "success", "report": report}

class IntelligenceAgent(BaseAgent):
    def __init__(self, name: str = "Intelligence"):
        super().__init__(name)
        self.memory_file = "agent_memory.json"
        self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    self.persistent_memory = json.load(f)
            except:
                self.persistent_memory = {"runs": 0, "history": []}
        else:
            self.persistent_memory = {"runs": 0, "history": []}

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.persistent_memory, f, indent=2)

    async def process(self, data: dict) -> dict:
        """
        Orchestrate or Summarize.
        Expects a 'summary_report' from the orchestrator containing all other agents' outputs.
        """
        self.log("Processing mission intelligence...")

        run_data = data.get("run_data", {})

        # Learning: Update run count
        self.persistent_memory["runs"] += 1

        # Store a summary of this run
        run_summary = {
            "run_id": self.persistent_memory["runs"],
            "timestamp": datetime.now().isoformat(),
            "health": run_data.get("health", {}).get("overall_status"),
            "roi": run_data.get("monetization", {}).get("projected_roi")
        }
        self.persistent_memory["history"].append(run_summary)

        # Keep history small
        if len(self.persistent_memory["history"]) > 10:
            self.persistent_memory["history"].pop(0)

        self.save_memory()

        decision = "CONTINUE"
        if run_summary["health"] == "Critical":
            decision = "HALT"

        self.log(f"Intelligence updated. Total Runs: {self.persistent_memory['runs']}. Decision: {decision}")

        return {"status": "success", "decision": decision}
