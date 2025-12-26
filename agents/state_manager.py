import json
import os

class StateManager:
    def __init__(self, filepath='agents/agent_state.json'):
        self.filepath = filepath
        self.state = self.load_state()

    def load_state(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                pass

        # Default state
        return {
            "system_iq": 25.0,  # Starting IQ as requested
            "total_cycles": 0,
            "last_active": None
        }

    def save_state(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.state, f, indent=4)

    def get_iq(self):
        return self.state.get("system_iq", 25.0)

    def evolve_iq(self, increment=0.1):
        """
        Simulate self-learning and improvement.
        """
        self.state["system_iq"] += increment
        self.state["system_iq"] = round(self.state["system_iq"], 2)
        self.save_state()
        return self.state["system_iq"]

    def increment_cycle(self):
        self.state["total_cycles"] += 1
        self.save_state()

if __name__ == "__main__":
    sm = StateManager()
    print(f"Current IQ: {sm.get_iq()}")
    sm.evolve_iq()
    print(f"Evolved IQ: {sm.get_iq()}")
