from .base_agent import BaseAgent
import json
import os
import datetime

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence Agent")
        self.memory_file = "intelligence_memory.json"
        self.memory = self.load_memory()

    def load_memory(self):
        default_memory = {
            "iq": 25.0,
            "last_run": None,
            "total_runs": 0,
            "insights_generated": 0
        }
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                return default_memory
        return default_memory

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f)

    def learn(self, data, found_targets):
        """Self-improvement logic to increase IQ based on performance."""
        # 1. Base experience for showing up
        iq_gain = 0.1

        # 2. Learning from data volume
        if data:
            iq_gain += min(len(data) * 0.001, 0.5) # Cap data gain

        # 3. Value from insights
        total_targets = sum(found_targets.values())
        if total_targets > 0:
            iq_gain += min(total_targets * 0.05, 1.0) # Cap insight gain

        # Apply growth
        self.memory["iq"] = round(self.memory["iq"] + iq_gain, 4)
        self.memory["total_runs"] += 1
        self.memory["last_run"] = datetime.datetime.now().isoformat()
        self.memory["insights_generated"] += total_targets

        self.save_memory()
        return iq_gain

    def run(self, data, context=None):
        self.log(f"Gathering intelligence... (Current IQ: {self.memory['iq']})")

        # Identify high-value targets (e.g., .gov or .edu domains, or specific tech giants)
        high_value_domains = ['google', 'amazon', 'facebook', 'apple', 'microsoft']
        found_targets = {}

        for p in data:
            domain = p.get('domain', '')
            if domain:
                for target in high_value_domains:
                    if target in domain:
                        found_targets[target] = found_targets.get(target, 0) + 1

        report = "### Market Intelligence\n"

        # Calculate IQ Gain
        gain = self.learn(data, found_targets)

        report += f"**System IQ:** {self.memory['iq']} (+{gain:.4f} gain)\n"
        report += f"**Evolution Status:** Self-learning active. Runs: {self.memory['total_runs']}\n\n"

        report += "**Competitor/Tech Giant Activity:**\n"
        for target, count in found_targets.items():
            report += f"- {target.capitalize()}: {count} links found\n"

        self.log(f"Intelligence gathering complete. New IQ: {self.memory['iq']}")
        return report
