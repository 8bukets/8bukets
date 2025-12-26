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
        default_memory = {
            "runs": 0,
            "iq": 25,  # Starting IQ
            "weights": {
                "bid_aggressiveness": 1.0,
                "creativity_threshold": 0.5
            },
            "history": []
        }
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    self.persistent_memory = json.load(f)
                    # Ensure new keys exist if loading old memory
                    for key, val in default_memory.items():
                        if key not in self.persistent_memory:
                            self.persistent_memory[key] = val
            except:
                self.persistent_memory = default_memory
        else:
            self.persistent_memory = default_memory

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.persistent_memory, f, indent=2)

    def get_mission_strategy(self) -> dict:
        """
        Returns the strategy for the upcoming run based on learned weights.
        """
        self.log(f"Generating mission strategy. Current IQ: {self.persistent_memory['iq']}")
        return {
            "iq": self.persistent_memory["iq"],
            "bid_aggressiveness": self.persistent_memory["weights"]["bid_aggressiveness"],
            "creativity_threshold": self.persistent_memory["weights"]["creativity_threshold"]
        }

    async def process(self, data: dict) -> dict:
        """
        Orchestrate or Summarize.
        Expects a 'summary_report' from the orchestrator containing all other agents' outputs.
        """
        self.log("Processing mission intelligence...")

        run_data = data.get("run_data", {})

        # Learning: Update run count
        self.persistent_memory["runs"] += 1

        # Analyze performance
        roi_str = run_data.get("monetization", {}).get("projected_roi", "0%")
        try:
            roi = float(roi_str.replace('%', ''))
        except ValueError:
            roi = 0.0

        health = run_data.get("health", {}).get("overall_status", "Unknown")

        # Self-Improvement Logic (Learning)
        iq_gain = 0

        # Reward high ROI
        if roi > 20:
            iq_gain += 1
            # If profitable, be slightly more aggressive next time
            self.persistent_memory["weights"]["bid_aggressiveness"] = min(2.0, self.persistent_memory["weights"]["bid_aggressiveness"] + 0.05)
        elif roi < 0:
            iq_gain -= 0.5
            # If losing money, be more conservative
            self.persistent_memory["weights"]["bid_aggressiveness"] = max(0.5, self.persistent_memory["weights"]["bid_aggressiveness"] - 0.05)

        # Reward System Health
        if health == "Healthy":
            iq_gain += 0.1
        else:
            iq_gain -= 1.0

        # Update IQ
        self.persistent_memory["iq"] = round(self.persistent_memory["iq"] + iq_gain, 2)

        # Store a summary of this run
        run_summary = {
            "run_id": self.persistent_memory["runs"],
            "timestamp": datetime.now().isoformat(),
            "health": health,
            "roi": roi_str,
            "resulting_iq": self.persistent_memory["iq"]
        }
        self.persistent_memory["history"].append(run_summary)

        # Keep history small
        if len(self.persistent_memory["history"]) > 20:
            self.persistent_memory["history"].pop(0)

        self.save_memory()

        decision = "CONTINUE"
        if health == "Critical":
            decision = "HALT"

        self.log(f"Intelligence updated. Total Runs: {self.persistent_memory['runs']}. New IQ: {self.persistent_memory['iq']}. Decision: {decision}")

        return {"status": "success", "decision": decision, "iq": self.persistent_memory["iq"]}
