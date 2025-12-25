import json
import os
from datetime import datetime

class Memory:
    def __init__(self, filepath="memory.json"):
        self.filepath = filepath
        self.data = {
            "facts": {},
            "experiences": [],
            "performance_metrics": {},
            "ad_campaigns": []
        }
        self.load()

    def load(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    self.data = json.load(f)
            except json.JSONDecodeError:
                print("Memory file corrupted, starting fresh.")

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)

    def remember_fact(self, key, value):
        self.data["facts"][key] = value
        self.save()

    def get_fact(self, key):
        return self.data["facts"].get(key)

    def log_experience(self, agent_name, action, outcome, score):
        experience = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent_name,
            "action": action,
            "outcome": outcome,
            "score": score
        }
        self.data["experiences"].append(experience)
        self.save()

    def get_experiences(self, agent_name=None):
        if agent_name:
            return [e for e in self.data["experiences"] if e["agent"] == agent_name]
        return self.data["experiences"]

    def update_metric(self, metric, value):
        self.data["performance_metrics"][metric] = value
        self.save()
